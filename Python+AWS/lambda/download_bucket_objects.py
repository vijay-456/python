import boto3
import base64

s3_client = boto3.client('s3')

def pandu(event, context):
    fileObj = s3_client.get_object(Bucket='pandu-pics', Key='destination_1.jpg')
    content = fileObj["Body"].read()
    return base64.b64encode(content)

