import boto3

class dynamoDBTable:
    def __init__(self):
        self.resource = boto3.resource('dynamodb') 
        
    def dynamo_data(self, tableName, alarmName, date):
        table = self.resource.Table(tableName)
        values = {}
        values['id'] = alarmName
        values['AlarmCreatedDate'] = date
        
        table.put_item(Item = values)