from aws_cdk import (
    
    aws_lambda as lambda_,
    aws_events as events_,
    aws_events_targets as targets_,
    aws_s3 as S3_,
    aws_s3_deployment as S3_deploy,   
    Stack,
 
)
from constructs import Construct


class ShazeelSprint1Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        

        
        
        #function call for webHealthLambda 
        '''
        parameters
        id
        path of lambda file i.e. assest
        lambda handler
        '''
        webHealth_lambda = self.create_lambda("Shazeel_webHealthLambda", "./resources", "WebHealth_Lambda.lambda_handler")
        
        
        # creating an S3 bucket
        '''
        parameters
        name of the bucket
        '''
        my_bucket = self.create_bucket("Shazeel_skipq")
        
        #uploading file to s3 bucket
         '''
        parameters
        variable having bucket stored in it
        path of the file that being uploded
        '''
        
        self.upload_file(my_bucket,"./resources")
        
        #setting a schedule of one minute
         '''
        parameters
        targetsLambda:
        handler having a function call of webHealth_lambda
        
        rule:
        id
        description
        scheduleLambda 
        targetsLambda
        '''
        scheduleLambda=events_.Schedule.cron()
        targetsLambda=targets_.LambdaFunction(handler=webHealth_lambda)
        rule = events_.Rule(self, "webHealthInvocation",description= "Periodic webHealth Lambda", schedule=scheduleLambda, targets=[targetsLambda])
        
        
        
    
    #creating lambda
     '''
        parameters
        id
        asset
        handler
        '''
    
    def create_lambda(self, id, asset,handler):
        return  lambda_.Function(self, id,
        code=lambda_.Code.from_asset(asset),
        runtime=lambda_.Runtime.PYTHON_3_6,
        handler=handler
    )
    
    # code for creating Bucket
   
    def create_bucket(self, bucketName):
      my_bucket=S3_.Bucket(self, bucketName) 
      return my_bucket
    
    
     #code for uploading a file
     
    def upload_file(self, my_bucket, path):
        S3_deploy.BucketDeployment(self, "urlFile",
        sources=[S3_deploy.Source.asset(path)],destination_bucket=my_bucket)
