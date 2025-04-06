import requests
import json
import os
import pandas as pd
import awswrangler as wr
import boto3 
from dotenv import load_dotenv
from jobicy_data import response

jobs = response['jobs']
df = pd.json_normalize(jobs)
#AWS credentials
aws_access_key_id = os.getenv('ACCESS_KEY')
aws_secret_access_key = os.getenv('SECRET_KEY')
aws_region = os.getenv('region')

session = boto3.Session(
    aws_access_key_id= aws_access_key_id,
    aws_secret_access_key= aws_secret_access_key,
    region_name=  aws_region
)

#the S3 path where the Parquet file will be saved
path_s3 = 's3://kayceesecondassignment/JobMarketingn.parquet'

# Upload the DataFrame to S3 as a Parquet file using awswrang
wr.s3.to_parquet(
    df= df,
    path=path_s3,
    dataset=True,  
    mode='append',
    boto3_session=session 
)