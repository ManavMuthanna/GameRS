from bs4 import BeautifulSoup
import requests
import pandas as pd

user_agent = {'User-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'}

page = 0
pages = []
count = 0
while (page != 72):
    url = f"https://www.metacritic.com/browse/games/release-date/available/pc/metascore?view=detailed%2F&page={page}"
    page = page + 1
    pages.append(url)
    count = count+1

pages_df = pd.DataFrame(pages, columns=['Pages'])
pages_df.to_csv("Pages.csv")

final_list = []
final_img_list = []

len_pages = len(pages_df['Pages'].tolist())

count_l = 0
#change number to len_pages
for i in range(0,2):
    count_l = count_l +1
    print(count_l)
    url = pages_df["Pages"][i]
    
    response = requests.get(url, headers = user_agent)

    soup = BeautifulSoup(response.text, 'html.parser')
    link_dict = {'Link' : []}
    final_url_df = pd.DataFrame(link_dict)    
    # name_df = pd.DataFrame(name_list,columns=['Name'])
    # genre_df = pd.DataFrame(genre_list,columns=['Genre'])
    # dev_df = pd.DataFrame(dev_list,columns=['Developer'])
    # summary_df = pd.DataFrame(summary_list,columns=['Summary'])

    def get_url():
        count = 0
        list1 = soup.find('div', class_='browse_list_wrapper one browse-list-large').find_all('tr')

        for game in list1:
            list_url = game.find('a', class_='title')
            if(list_url == None):
                continue
            else:
                count = count + 1
                list_url = list_url.get('href')
                final_list.append(list_url)
            
        list2 = soup.find('div', class_='browse_list_wrapper two browse-list-large').find_all('tr')

        for game in list2:
            list_url = game.find('a', class_='title')
            if(list_url == None):
                continue
            else:
                count = count + 1
                list_url = list_url.get('href')
                final_list.append(list_url)

        list3 = soup.find('div', class_='browse_list_wrapper three browse-list-large').find_all('tr')

        for game in list3:
            list_url = game.find('a', class_='title')
            if(list_url == None):
                continue
            else:
                count = count + 1
                list_url = list_url.get('href')
                final_list.append(list_url)

        list4 = soup.find('div', class_='browse_list_wrapper four browse-list-large').find_all('tr')

        for game in list4:
            list_url = game.find('a', class_='title')
            if(list_url == None):
                continue
            else:
                count = count + 1
                list_url = list_url.get('href')
                final_list.append(list_url)

        url_df = pd.DataFrame(final_list,columns = ['Links'])
        url_df.to_csv("Links.csv")
        print("Got /Links!")

    get_url()

    
