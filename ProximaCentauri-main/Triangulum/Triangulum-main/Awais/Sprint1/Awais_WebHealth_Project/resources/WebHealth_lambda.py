import datetime
import urllib3
import boto3
import json
import keys as keys

def lambda_handler(event, context):
    
   values = []
   
   #Setting up voto3 client to access the s3 bucket
   client = boto3.client(
    's3',
    aws_access_key_id = keys.aws_access_key_id,
    aws_secret_access_key = keys.aws_secret_access_key,
    region_name = 'us-east-2')
    
 
    
    # Fetch the list of existing buckets
   clientResponse = client.list_buckets()
    
    # Create the S3 object
   obj = client.get_object(
    Bucket='awaiswebhealthbucket',
    Key='links.json'
    )

    
    # Read data from the S3 object
   data = obj['Body'].read()
   y = json.loads(data)
   links = []
   
   #Passing data to get_availability and get_latency functions
   for link in y['URLS_TO_MONITOR']:
       links.append(link)
       print(link)
       avail = get_availability(link)
       latency = get_latency(link)
        
       values.append({'Status':link,"availability": avail, "latency": latency})
        
   return values   
   
    
def get_availability(url):
    ### Returns 1.0 if available and 0 if not
    http = urllib3.PoolManager()
    response = http.request("GET", url)
    if response.status == 200:
        return 1.0
    else:
        return 0.0


def get_latency(url):
    ### Returns latency in seconds
    http = urllib3.PoolManager()
    start = datetime.datetime.now()
    response = http.request("GET", url)
    end = datetime.datetime.now()
    delta = end - start
    latencySec = round(delta.microseconds * .000001, 6)
    return latencySec
