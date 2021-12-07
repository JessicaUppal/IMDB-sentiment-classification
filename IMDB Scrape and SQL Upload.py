import bs4
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
from splinter import Browser
import requests
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager

####### Go to webpage and scrape data ########

# Chrome Browser
browser = Browser('chrome', executable_path=ChromeDriverManager().install(), headless=False)

# URL of page to be scraped
url = 'https://www.imdb.com/list/ls016522954/?ref_=nv_tvv_dvd'


# Retrieve page with the requests module
response = requests.get(url)

# Create BeautifulSoup object; parse with 'html.parser'
soup = BeautifulSoup(response.text, 'html.parser')

# Get all div's with the class "caption"
results = soup.find_all('h3',class_="lister-item-header")

# Loop through returned results
for result in results:
    # Error handling
    try:
        # Identify and return title of listing
        title = result.a.text
        # Identify and return link to listing
        link = result.a['href']

        # Print results only if title, price, and link are available
        if (title and link):
            print('-------------')
            print(title)
            print(link)
    except AttributeError as e:
        print(e)

# declare start and end URL variables      
url2 = 'https://www.imdb.com'
url3 = "reviews?ref_=ttls_li_tt"

#create empty list to collect values
film_reviews = []

# Loop through returned results
for result in results:
    try:
        title = result.a.text
        print(title)
        link = result.a["href"]
        print(url2+link+url3)
        browser.visit(url2 + link + url3)
        
        html = browser.html
        
        soup = BeautifulSoup(html, 'html.parser')
        
        content = soup.find('div', class_="lister-list")
        
        review = content.find('div', class_="text")
        print(review.text)

        # create empty dictionary to collect results
        review_dict = dict()
        # append values to empty dictionary
        review_dict['title'] = title
        review_dict['url'] = url2 + link + url3
        review_dict['review'] = review.text
        # append each dictionary into the empty film_reviews list
        film_reviews.append(review_dict)
            
    except AttributeError as e:
        print(e)

browser.quit()        

#install pymysql module to connect with MySQL Database

pip install pymysql
import pymysql

# Store credantials in file my.properties and use Config parser to read from it
import configparser
config = configparser.RawConfigParser()
config.read(filenames = 'my.properties')
print(config.sections())

h = config.get('mysql','host')
u = config.get('mysql','user')
p = config.get('mysql','password')
db = config.get('mysql','database')


# Open database connection
scrap_db = pymysql.connect(h,u,p,db)

# prepare a cursor object using cursor() method
cursor = scrap_db.cursor()

# Drop table if it already exist using execute() method.
#cursor.execute("DROP TABLE IF EXISTS IMDB_REVIEWS")

# Create table as per requirement
#sql = """CREATE TABLE IMDB_REVIEWS (
 #TITLECHAR(100),
 #URLCHAR(1000),
 #REVIEWCHAR(1000)
 #)"""

cursor.execute(sql)
#Save data to the table

scrap_db = pymysql.connect(h,u,p,db)
mySql_insert_query = """INSERT INTO IMDB_REVIEWS (TITLE, URL, REVIEW, SENTIMENT) 
VALUES (%s, %s, %s, %s ,%s, %s, %s) """

records_to_insert = film_reviews

cursor = scrap_db.cursor()
cursor.executemany(mySql_insert_query, records_to_insert)
scrap_db.commit()
print(cursor.rowcount, "Record inserted successfully into IMDB_REVIEWS table")

# disconnect from server
scrap_db.close()