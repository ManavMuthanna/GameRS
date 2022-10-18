#running get_links.py
from get_links import get_url

import os
import pandas as pd
from google.cloud import storage

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="<project-key>.json"
bucket_name = 'game-rec-files'

#uploading to bucket
def upload_to_storage(bucket_name: str, source_file_path: str, destination_blob_path: str):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_path)
    blob.upload_from_filename(source_file_path)
    print(f'The file {source_file_path} is uploaded to GCP bucket path: {destination_blob_path}')
    return None

def upload_links():
    source_files = ['Links.csv','Pages.csv']
    destination_blobs = ['Links.csv','Pages.csv']
    length = len(source_files)
    for i in range(0,length):
        source_file = source_files[i]
        destination_blob = destination_blobs[i]
        upload_to_storage(bucket_name, source_file, destination_blob)

upload_links()

#running resources.py
from resources import main

def upload_resources():
    source_files = ['Names.csv','Final_Links.csv','img_links.csv', 'Genres.csv', 'Developer.csv', 'Summary.csv']
    destination_blobs = ['Names.csv','Final_Links.csv','img_links.csv', 'Genres.csv', 'Developer.csv', 'Summary.csv']
    length = len(source_files)
    for i in range(0,length):
        source_file = source_files[i]
        destination_blob = destination_blobs[i]
        upload_to_storage(bucket_name, source_file, destination_blob)

upload_resources()
