import boto3

client = boto3.client('s3')

response = client.create_bucket(
    Bucket='mashood-s3-exam-456',
    CreateBucketConfiguration={
    'LocationConstraint': 'ap-south-1'
    }
)
