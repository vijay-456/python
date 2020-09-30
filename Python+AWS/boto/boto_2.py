import boto3

s3 = boto3.client('s3')

s3.download_file('pandu-pics','srinu.txt','check_2')
