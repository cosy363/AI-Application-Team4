from scrap_url import scrap_url
from scrap_product import scrap_product
import csv

##Inital Setting
#Before Start, go to scrap_url.py and change local address for chromedriver

#URL LOADTIME -> Time needed to wait until all products are loaded
url_loadtime = 0.1 

#ITERATION NUM -> Number of products that are scrapped for each URLS
iteration_num = 2

#URLS -> URL for scrapping; each URLs needs to have all products in its page, therefore change "?page" num to approporiate number(ex.200).
urls = ["https://www.ikea.com/kr/ko/cat/lamps-li002/?page=100","https://www.ikea.com/kr/ko/cat/bookcases-shelving-units-st002/?page=50","https://www.ikea.com/kr/ko/cat/cabinets-cupboards-st003/?page=100","https://www.ikea.com/kr/ko/cat/chests-of-drawers-drawer-units-st004/?page=50","https://www.ikea.com/kr/ko/cat/rugs-10653/?page=50","https://www.ikea.com/kr/ko/cat/tables-desks-fu004/?page=52","https://www.ikea.com/kr/ko/cat/beds-bm003/?page=100","https://www.ikea.com/kr/ko/cat/chairs-fu002/?page=150","https://www.ikea.com/kr/ko/cat/wardrobes-19053/?page=2"]

#URL NAMES -> Name of csv files for each URLs
url_names = ["lamp","bookcase","cabinet","drawer","rug","table","bed","chair","wardrobe"]

##Scrapping
for i, url in enumerate(urls):
    #Scrap Product URL from Category URL
    url_list = scrap_url(url,url_loadtime)

    #Scrap Product Details from Product URL
    product_list = scrap_product(url_list,iteration_num)

    #Save product list-dictionary to CSV file
    keys = product_list[0].keys()
    text = url_names[i] + '.csv'
    a_file = open(text, "w")
    dict_writer = csv.DictWriter(a_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(product_list)
    a_file.close()
    print("-> Product Catalogue Saved as " + url_names[i] + ".csv")