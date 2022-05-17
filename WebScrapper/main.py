from scrap_url import scrap_url
from scrap_product import scrap_product
import csv
import json

#Inital Setting
url_loadtime = 180
iteration_num = 3000
urls = ["https://www.ikea.com/kr/ko/cat/lamps-li002/?page=50","https://www.ikea.com/kr/ko/cat/bookcases-shelving-units-st002/?page=50","https://www.ikea.com/kr/ko/cat/cabinets-cupboards-st003/?page=100","https://www.ikea.com/kr/ko/cat/chests-of-drawers-drawer-units-st004/?page=50","https://www.ikea.com/kr/ko/cat/rugs-10653/?page=50","https://www.ikea.com/kr/ko/cat/tables-desks-fu004/?page=52",]
url_names = ["lamp","bookcase","cabinet","drawer","rug","table"]

for i, url in enumerate(urls):
    #Scrap Product URL from Category URL
    url_list = scrap_url(url,url_loadtime)

    #Scrap Product Details from Product URL
    product_list = scrap_product(url_list,iteration_num)

    print(i)
    #Save product list-dictionary to CSV file
    if i == 0:
        keys = product_list[0].keys()
    
    text = 'data.csv'
    # text = str(i) + '.csv'
    a_file = open(text, "w")
    dict_writer = csv.DictWriter(a_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(product_list)
    a_file.close()
    print("-> Product Catalogue Saved as output.csv")