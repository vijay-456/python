import boto3
#import botocore

s3 = boto3.resource('s3')

s3.Bucket('pandu-pics').download_file('srinu.txt','check_1')
