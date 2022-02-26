import urllib3
import datetime
import boto3
import sys


# importing a file having access key and private key
import security_credentials as keys

'''
creating a object of boto3 client to download the file from s3 bucket

download_file:
parameters
bucket name
file name with file to be downloaded
path from which the file will be downloaded

'''
def lambda_handler(event, context):
    s3=boto3.client('s3',  aws_access_key_id=keys.Access_Key,
    aws_secret_access_key=keys.Secret_Key)
    s3.download_file('shazeelsprint1stack-shazeelskipq20b06f9d-1ncd0w5j825o7','constant.py', '/tmp/constant.py')
    
    sys.path.insert(1, '/tmp/')
    
    #importing a constatnt file
    
    import constant
    
    #accesing the urls present in constant file saved in 
    #list named as URL_TO_MONITOR
    
    
    links = constant.URL_TO_MONITOR
    
    
    
    results=[]
    
    for url in links:
   
        avail = get_availability(url)
        latency = get_latency(url)
        results.append({"link" : url, "availability" :avail, "latency" : latency})
        
    return results
    #get_availability
    '''
    parameters:
    url : link to check the availability
    
    '''
    
def get_availability(url):
    http = urllib3.PoolManager()
    response = http.request("GET", url)
    if response.status == 200:
        return 1.0
    else:
        return 0.0

 #get_latency
    '''
    parameters:
    url : link to check the latency
    
    '''
def get_latency(url):
    http = urllib3.PoolManager()
    startTime=datetime.datetime.now()
    response = http.request("GET", url)
    endTime=datetime.datetime.now()
    delta = endTime - startTime             #time difference
    latencySec = round(delta.microseconds * .000001,6)
    return latencySec

