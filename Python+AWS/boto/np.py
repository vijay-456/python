import json
import boto3
from boto3.dynamodb.conditions import Key#,Attr

def lambda_handler():
    print('hai')
    dynamodb_client = boto3.resource('dynamodb')
    '''table = dynamodb_client.Table('S3_Objects_Upload')
    
    #Getting an item using a key
    response = table.get_item(
        Key = {
            'Key' : 'sam.pdf',
        },
        )
        
    #tab = boto3.client('dynamodb').Table('S3_Objects_Upload')    
    #Getting multiple items using query and resource
    response = table.query(
        KeyConditionExpression=Key('Key').lt(99999)
        )
    
    print(response['Item'])
    return response['Item']
    '''
print(lambda_handler())
