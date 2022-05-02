from selenium import webdriver
from bs4 import BeautifulSoup
import time
from tempfile import TemporaryFile
import numpy as np

## Initial Value
# Put in url for furniture category

def scrap_url(url,load_time):
    driver = webdriver.Chrome('/Users/brannynew/Documents/AIStartup/WebScrapper/chromedriver 2')
    driver.get(url)
    time.sleep(load_time)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()

    link = []

    product_list = soup.find_all("div",{"class":"pip-product-compact"})

    for product in product_list:
        anchor = product.find("a")
        link.append(anchor["href"])

    # Print product numbers
    print("Number of products: ",len(link))

    return link
    