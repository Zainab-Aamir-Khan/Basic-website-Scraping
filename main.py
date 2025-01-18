# for scraping data, we can use two methods
# 1. use API
# 2. use tools like bs4

#Step : 1 # install the following

# pip install requests
# pip install BeautifulSoup
# pip install html5lib

import requests
from bs4 import BeautifulSoup
url = "https://www.codewithharry.com/"

#step : 2 Get the HTML

r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

# Step : 3 Parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify())

# Step : 3 HTML tree traversal
title = soup.title
#commonly used type objects
# print(type(title)) # 1.title
# print(type(title.string)) # 2.navigable string
# print(type(soup)) # 3.soup

#get the title of the HTML page
print(title)

#get all the paragraphs of the page
# paras = soup.find_all('p')
# print(paras)

#get all the anchor tags of the page
# anchor = soup.find_all('a')
# print(anchor)

#get the first paragraph of the page
# print(soup.find('p'))
firstPara = soup.find('p')
print(firstPara.text)

#get the class of the any element in HTML page
print(soup.find('p')['class'])





  





