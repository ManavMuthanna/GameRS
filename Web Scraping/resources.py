from bs4 import BeautifulSoup
import requests
import pandas as pd
from google.cloud import storage
import io
from io import BytesIO
from urllib3 import Retry
from requests.adapters import HTTPAdapter, Retry

from datetime import datetime

script_start_time = datetime.now()

user_agent = {'User-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'}

storage_client = storage.Client.from_service_account_json("<project-key>.json")
bucket_name = '<bucket name>'
bucket = storage_client.get_bucket(bucket_name)

pages_bucket = bucket.blob("Pages.csv")
pages_data = pages_bucket.download_as_string()
pages = pd.read_csv(io.BytesIO(pages_data), encoding='utf-8', sep = ' ')

links_bucket = bucket.blob("Links.csv")
links_data = links_bucket.download_as_string()
links = pd.read_csv(io.BytesIO(links_data), encoding='utf-8', sep = ',')

final_list = links['Links'].tolist()

name_list = []
genre_list = []
dev_list = []
summary_list = []
final_urls = []

#running get_img.py
from get_img import get_img_url
from get_img import final_img_list

session = requests.Session()
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)

def get_data(static_page):

        response2 = session.get(static_page, headers = user_agent)

        soup2 = BeautifulSoup(response2.text, 'html.parser')
        
        name = soup2.find('div', class_= "product_title")
        if(name != None):
            final_urls.append(static_page)
            get_img_url(static_page)
            name = name.find('a')
            name = name.text
            name_list.append(name)

            genre = soup2.find('li', class_= "summary_detail product_genre")
            if(genre == None):
                genre = 'N/A'
                genre_list.append(dev)
            else: 
                genre = genre.text
                genre_list.append(genre)

            dev = soup2.find('li', class_= "summary_detail developer")
            if(dev == None):
                dev = 'N/A'
                dev_list.append(dev)
            else: 
                dev = dev.text
                dev_list.append(dev)

            summary = soup2.find('li', class_= "summary_detail product_summary")
            if(summary==None):
                summary = 'N/A'
                summary_list.append(summary)
            else:
                summary = soup2.find('li', class_= "summary_detail product_summary").find('span', class_="blurb blurb_expanded")
                if(summary == None):
                    summary = soup2.find('li', class_= "summary_detail product_summary").find('span', class_="data")
                    summary = summary.text
                    summary_list.append(summary)
                else:
                    summary = summary.text
                    summary_list.append(summary)
        else:
            exit

def main():
    length = len(final_list)
    count_l = 0
    for i in range(0,length):
        count_l = count_l+1
        print(count_l)
        link = final_list[i]
        static_page = "https://www.metacritic.com" + link
        print(link)
        get_data(static_page)

    final_links_df = pd.DataFrame(final_urls,columns=['Link'])
    name_df = pd.DataFrame(name_list,columns = ['Name'])
    genre_df = pd.DataFrame(genre_list,columns = ['Genre'])
    dev_df = pd.DataFrame(dev_list,columns = ['Developer'])
    summary_df = pd.DataFrame(summary_list,columns = ['Summary'])
    img_df = pd.DataFrame(final_img_list,columns = ['Img_Links'])

    img_df.to_csv("img_links.csv", mode='a', index=True, header=False)
            
    final_links_df.to_csv('Final_Links.csv', mode='a', index=True, header=False)

    name_df.to_csv("Names.csv", mode='a', index=True, header=False)

    genre_df.to_csv("Genres.csv", mode='a', index=True, header=False)   

    dev_df.to_csv("Developer.csv", mode='a', index=True, header=False)

    summary_df.to_csv("Summary.csv", mode='a', index=True, header=False)         


main()

print('!!!!DONE!!!!')
script_end_time = datetime.now()
final_time = script_end_time - script_start_time
print("Time Taken: ", final_time)