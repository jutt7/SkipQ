import boto3
from botocore.exceptions import NoCredentialsError

def lambda_handler(event, context):
    s3_client = boto3.client('s3')

   # response = s3_client.upload_file('./resources/requirements.txt','awaiswebhealthbucket','requirements.txt')
    response = s3_client.upload_file('requirements.txt', 'awaiswebhealthbucket', 's3_file_name')
    
    uploaded = upload_to_aws('requirements.txt', 'awaiswebhealthbucket', 'requirements.txt')
    
def upload_to_aws(local_file, bucket, s3_file):
    s3 = boto3.client('s3', aws_access_key_id='AKIAUTEXLE6CCDHCAN7P',
                      aws_secret_access_key='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')

    try:
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False 