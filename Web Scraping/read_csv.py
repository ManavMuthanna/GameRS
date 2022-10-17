import os
import io
import pandas as pd
from google.cloud import storage

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="<project-key>.json"
bucket_name = 'game-rec-files'

#uploading to bucket
def read_from_storage(source_file_path: str):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(source_file_path)
    data = blob.download_as_string()
    df = pd.read_csv(io.BytesIO(data))
    print(f'Pulled down file from bucket {bucket_name}, file name: {source_file_path}')
    print(df.head())
    return None

read_from_storage("<bucket-path>/Names.csv")