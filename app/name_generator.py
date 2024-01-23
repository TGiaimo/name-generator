import requests
from bs4 import BeautifulSoup
from textblob import TextBlob

def generate(number):
  article_titles = []
  if(number == 0):
    url = "https://www.npr.org/sections/strange-news/"
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="main-section")

    article_titles = results.find_all("h2", class_="title")
  
  if(number == 1):
    url = "https://apnews.com/oddities/"
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(class_="Page-oneColumn")
    
    article_titles = results.find_all("span", class_="PagePromoContentIcons-text")
    
  titles_list = []
  
  for article_title in article_titles:
      title = TextBlob(article_title.text.strip().replace("'", "").replace("—", "").replace("’", "").replace("‘", "").replace("$", ""))
      for np in title.noun_phrases:
        titles_list.append(str(np))
        print(str(np))
  titles_list = list(set(titles_list))
  return titles_list

generate(1)