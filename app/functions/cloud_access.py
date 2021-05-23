import os
from google.cloud import storage
from google.cloud.storage import bucket



def get_storage_client():
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'ServiceKey_GoogleCloud.json'
    storage_client = storage.Client()
    return storage_client

def create_bucket():
    storage_client = get_storage_client()
    bucket_name = 'cloud_storage_sachin'
    bucket = storage_client.bucket(bucket_name=bucket_name)
    bucket.location = "US"
    bucket = storage_client.create_bucket(bucket)
    return bucket

def get_bucket():
    storage_client = get_storage_client()
    bucket = storage_client.get_bucket("cloud_storage_sachin")
    return bucket