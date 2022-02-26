from aws_cdk import (
    aws_lambda as lambda_,
    aws_events as events_,
    aws_events_targets as targets_,
    aws_s3 as s3,
    aws_iam as iam,
    aws_s3_deployment as s3deploy,
    # Duration,
    Stack,
    # aws_sqs as sqs,
)
from constructs import Construct

class AwaisWebHealthProjectStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        #Created s3 bucket
        
        myBucket = s3.Bucket(self, 'MyFirstBucket', bucket_name='awaiswebhealthbucket')
        
        #uploaded file in s3 bucket
        
        s3deploy.BucketDeployment(self, "MyBucket",
        sources=[s3deploy.Source.asset("./URL")],
        destination_bucket=myBucket,
        )
        
        #createBucke = self.create_lambda("MyBucket","./resources","uploadFile.lambda_handler")
        
        HWLambda = self.create_lambda("MyHelloLambda","./resources","WebHealth_lambda.lambda_handler")
         
        scheduleLambda = events_.Schedule.cron()
        targetLambda = targets_.LambdaFunction(handler=HWLambda)
        rule = events_.Rule(self,"Webhealth_invocation_rule",description="Periodicaly invoked lambda", schedule=scheduleLambda,targets=[targetLambda])

       
        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "AwaisWebHealthProjectQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
    def create_lambda(self, newid, asset, handler):
        return lambda_.Function(self,id = newid,
        runtime = lambda_.Runtime.PYTHON_3_8,
        handler = handler,
        code = lambda_.Code.from_asset(asset),
        )
