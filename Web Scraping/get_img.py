from bs4 import BeautifulSoup
import requests
import pandas as pd

user_agent = {'User-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'}

final_img_list = []

def get_img_url(static_page):
        response = requests.get(static_page, headers = user_agent)

        soup = BeautifulSoup(response.text, 'html.parser')

        img = soup.find('div', class_= "product_image large_image must_play")
        count = 0
        count = count + 1
        img = img.find('img')
        img = img.get('src')
        final_img_list.append(img)

