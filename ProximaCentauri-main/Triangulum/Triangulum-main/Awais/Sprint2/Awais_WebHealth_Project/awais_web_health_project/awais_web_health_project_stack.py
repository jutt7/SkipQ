from aws_cdk import (
    aws_lambda as lambda_,
    aws_events as events_,
    aws_events_targets as targets_,
    aws_s3 as s3,
    aws_iam,
    aws_s3_deployment as s3deploy,
    aws_cloudwatch as cloudwatch_,
     aws_cloudwatch_actions as actions_,
    aws_sns as sns,
    aws_sns_subscriptions as subscriptions,
    # Duration,
    Stack,
    # aws_sqs as sqs,
)
from resources import constants as constants
from constructs import Construct

class AwaisWebHealthProjectStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        #Created s3 bucket
        
        #myBucket = s3.Bucket(self, 'MyFirstBucket', bucket_name='awaiswebhealthbucket')
        
        #uploaded file in s3 bucket
        
        # s3deploy.BucketDeployment(self, "MyBucket",
        # sources=[s3deploy.Source.asset("./URL")],
        # destination_bucket=myBucket,
        # )
        
        lambda_role = self.create_lambda_role() 
        
        HWLambda = self.create_lambda("MyHelloLambda","./resources","WebHealth_lambda.lambda_handler",lambda_role)
         
        scheduleLambda = events_.Schedule.cron()
        targetLambda = targets_.LambdaFunction(handler=HWLambda)
        rule = events_.Rule(self,"Webhealth_invocation_rule",description="Periodicaly invoked lambda", schedule=scheduleLambda,targets=[targetLambda])
        
        
        topic = sns.Topic(self,"AwaisWebHealthTopic")
        topic.add_subscription(subscriptions.EmailSubscription('muhammad.awais.gondal.skipq@gmail.com'))
        
        for link in constants.url:
            
            dimension = {'URL':link}
        
            availability_metric = cloudwatch_.Metric(namespace=constants.URL_MONITOR_NAMESPACE,metric_name=constants.URL_MONITOR_NAME_AVAILABILITY,dimensions_map=dimension)
        
            availability_alarm = cloudwatch_.Alarm(self, id="Availability_Alarm for:"+link,
             metric=availability_metric,
            comparison_operator=cloudwatch_.ComparisonOperator.LESS_THAN_THRESHOLD,
            threshold=1,
            evaluation_periods=1,
            datapoints_to_alarm=1
            )
            
            
            latency_metric = cloudwatch_.Metric(namespace=constants.URL_MONITOR_NAMESPACE,metric_name=constants.URL_MONITOR_NAME_LATENCY,dimensions_map=dimension)
        
            latency_alarm = cloudwatch_.Alarm(self, id="Latency_Alarm for:"+link,
             metric=latency_metric,
            comparison_operator=cloudwatch_.ComparisonOperator.GREATER_THAN_THRESHOLD,
            threshold=0.25,
            evaluation_periods=1,
            datapoints_to_alarm=1
            )
            
            availability_alarm.add_alarm_action(actions_.SnsAction(topic))
            latency_alarm.add_alarm_action(actions_.SnsAction(topic))
            
            
            
            
            
            
            
        # dimension = {'URL':constants.URL_TO_MONITOR}
        
        # availability_metric = cloudwatch_.Metric(namespace=constants.URL_MONITOR_NAMESPACE,metric_name=constants.URL_MONITOR_NAME_AVAILABILITY,dimensions_map=dimension)
        
        # availability_alarm = cloudwatch_.Alarm(self, id="Availability_Alarm",
        #      metric=availability_metric,
        #     comparison_operator=cloudwatch_.ComparisonOperator.LESS_THAN_THRESHOLD,
        #     threshold=1,
        #     evaluation_periods=1,
        #     datapoints_to_alarm=1
        #     )
            
            
        # latency_metric = cloudwatch_.Metric(namespace=constants.URL_MONITOR_NAMESPACE,metric_name=constants.URL_MONITOR_NAME_LATENCY,dimensions_map=dimension)
        
        # latency_alarm = cloudwatch_.Alarm(self, id="Latency_Alarm",
        #      metric=latency_metric,
        #     comparison_operator=cloudwatch_.ComparisonOperator.GREATER_THAN_THRESHOLD,
        #     threshold=0.25,
        #     evaluation_periods=1,
        #     datapoints_to_alarm=1
        #     )
            
        # availability_alarm.add_alarm_action(actions_.SnsAction(topic))
        # latency_alarm.add_alarm_action(actions_.SnsAction(topic))
        

       
        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "AwaisWebHealthProjectQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
        
    def create_lambda_role(self):
        lambdaRole = aws_iam.Role(self, "lambda-role",
        assumed_by=aws_iam.ServicePrincipal('lambda.amazonaws.com'),
        managed_policies=[
                    aws_iam.ManagedPolicy.from_aws_managed_policy_name('service-role/AWSLambdaBasicExecutionRole'),
                    aws_iam.ManagedPolicy.from_aws_managed_policy_name('CloudWatchFullAccess')
            ])
        return lambdaRole
        
        
    def create_lambda(self, newid, asset, handler,role):
        return lambda_.Function(self,id = newid,
        runtime = lambda_.Runtime.PYTHON_3_8,
        handler = handler,
        code = lambda_.Code.from_asset(asset),
        role=role
        )
