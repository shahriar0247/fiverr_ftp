from google.cloud import storage
from app.functions.cloud_access import get_bucket, get_storage_client


def upload_file(bytedata, content_type, filename):
    try:
        bucket = get_bucket()
        filename = str(filename)
        blob = bucket.blob(filename)
        blob.upload_from_string(bytedata, content_type=content_type)
        return True
    except Exception as e:
        print(e)
        return False

def download_file(filename):
    try:
        bucket = get_bucket()
        
        blob = bucket.blob(filename)
        binary = blob.download_as_bytes()
        return binary
    except Exception as e:
        print(e)
        return False
