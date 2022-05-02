from scrap_url import scrap_url
from scrap_product import scrap_product
import csv

#Inital Setting
url_loadtime = 1
iteration_num = 100
url = "https://www.ikea.com/kr/ko/cat/tables-desks-fu004/?page=52"

#Scrap Product URL from Category URL
url_list = scrap_url(url,url_loadtime)

#Scrap Product Details from Product URL
product_list = scrap_product(url_list,iteration_num)

#Save product list-dictionary to CSV file
keys = product_list[0].keys()
a_file = open("output.csv", "w")
dict_writer = csv.DictWriter(a_file, keys)
dict_writer.writeheader()
dict_writer.writerows(product_list)
a_file.close()
print("-> Product Catalogue Saved as output.csv")