import boto3
from lib.core.config import config

s3_client = boto3.client(
    "s3",
    aws_access_key_id=config.get("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=config.get("AWS_SECRET_ACCESS_KEY"),
    region_name=config.get("AWS_S3_REGION")
)
bucket_name = config.get("AWS_S3_BUCKET")
