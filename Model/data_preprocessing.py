import pandas as pd
import os
import pandas as pd
from google.cloud import storage

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="<project-key>.json"
bucket_name = '<bucket-name>'

#uploading to bucket
def upload_to_storage(bucket_name: str, source_file_path: str, destination_blob_path: str):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_path)
    blob.upload_from_filename(source_file_path)
    print(f'The file {source_file_path} is uploaded to GCP bucket path: {destination_blob_path}')
    return None


def prep():
    df = pd.read_csv("Names.csv", index_col=False , names=["rem","Name"])
    df = df.drop(df.columns[0], axis=1)

    links = pd.read_csv("Final_Links.csv", index_col=False, names=["rem","Link"])
    links = links.drop(links.columns[0], axis=1)

    genres = pd.read_csv("Genres.csv", index_col=False, names=["rem","Genres"])
    genres = genres.drop(genres.columns[0], axis=1)

    developers = pd.read_csv("Developer.csv", index_col=False, names=["rem","Developer"])
    developers = developers.drop(developers.columns[0], axis=1)

    summaries = pd.read_csv("Summary.csv", index_col=False , names=["rem","Summary"], lineterminator='\n')
    summaries = summaries.drop(summaries.columns[0], axis=1)

    img_links = pd.read_csv("img_links.csv", index_col=False, names=["rem","Img_Link"])
    img_links = img_links.drop(img_links.columns[0], axis=1)
    df = df.replace('\n','', regex=True)

    link_df = links['Link']
    df.loc[:,'Link'] = link_df
    
    summaries = summaries.replace('\n','', regex=True)
    summaries_df = summaries['Summary']
    df.loc[:,"Summary"] = summaries_df

    genres = genres.replace(' ','', regex=True)
    genres=genres.replace('\(','',regex=True).astype(str)
    genres=genres.replace('\)','',regex=True).astype(str)
    genres=genres.replace('\:','',regex=True).astype(str)
    genres = genres.replace('Genres','', regex=True)
    genres_df = genres['Genres']
    df.loc[:,'Genres'] = genres_df

    developers = developers.replace(' ','', regex=True)
    developers = developers.replace('\n','', regex=True)
    developers = developers.replace('Developer','', regex=True)
    developers=developers.replace('\:','',regex=True).astype(str)
    developers_df = developers['Developer']
    df.loc[:,'Developer'] = developers_df

    img_link_df = img_links['Img_Link']
    df.loc[:,'Img_Link'] = img_link_df
  
    print(df.head())
    print(df.tail())
    df.to_csv("Dataset.csv")
    upload_to_storage(bucket_name, "Dataset.csv", "Dataset.csv")
    

prep()
