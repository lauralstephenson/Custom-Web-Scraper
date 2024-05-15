import requests
from bs4 import BeautifulSoup


def scrapeBlogs():
  pageToScrape = requests.get("https://www.tapaway.com.au/blog")
  soup = BeautifulSoup(pageToScrape.text, "html.parser")
  authors = soup.findAll("span", attrs= {"class":"tQ0Q1A"})
  titles = soup.findAll("p", attrs= {"class":"bD0vt9 KNiaIk"})
  #views = soup.findAll("span", attrs= {"class":"eYQJQu"}) Don't need ths one at the moment
  
  for author, title in zip(authors, titles):
      print(author.text + " - " + title.text)

scrapeBlogs()