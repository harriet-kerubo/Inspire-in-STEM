import requests
from bs4 import BeautifulSoup as bs

user_name = "harriet-kerubo" #input("enter your username")
url = "https://github.com/"+user_name #input("Enter URL")
results = requests.get(url)

soup = bs(results.content,"html.parser")
profile_pic = soup.find('img',{'alt':'Avatar'})['src']
print(profile_pic)

#web scraping using python