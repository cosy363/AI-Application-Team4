import json
import pymysql
from single_rec import single_rec


#1.REST API 형식의 유저 요청 들어옴
#json structure
json_string='''{
    "id": 1,
    "username": "Bret",
    "furniture preference": [1,2,5,3],
    "color preference": [1,3,6,4]
}'''

json_object = json.loads(json_string)


#inputs: user color, furniture combination
user_preference = {}
user_preference['user_color'] = json_object['color preference']
user_preference['furniture_combination'] = json_object['furniture preference']

#2.rearrange furniture combination by 우선도
furniture_combination.sort()
print(furniture_combination[0])

#3. single rec
# Connect mysql server
conn, cur = None, None
conn = pymysql.connect(host='127.0.0.1',user='root',password='kimjin12',db='furniture_ikea',charset='utf8')
cur = conn.cursor

##3.1: prime가구

# import prime가구 category dB from mysql
cur.execute("SELECT * FROM furniture_detail WHERE furniture_category1 = '{}'".format(str(furniture_combination[0])))

furn_list = []
do_singlerec(furn_list,furniture_combination[0])

def do_singlerec(DB,category):
    for furn in furn_list:
        single_rec()

# single_rec.py 돌리기
# output: 10 Ps


##3.2: second가구 
# import third가구 category dB from mysql
# single_rec.py for each 10 Ps
# output: 80 PxS    
#3.3: third가구
# import third가구 category dB from mysql
# single_rec.py for each 80 PXS
# output: 400 PXSXT
#3.4: second가구
# import prime가구 category dB from mysql
# single_rec.py for 400 PXSXT
# output: 800 PXSXTXF
# output: PSTFs[product_number], sum of single_scores of combination
#  

#4. Combination Evaluation

#4.1 DL MODEL
##4.1.1 narrow down DB for RI model(난수 and singlescore 내림차순)
##4.1.2 DL model gogo
# from mysql, import color&category of each furniture of combination
# input: only color&category
# output: DL_score
#4.2 Overall Evaluation and Randomization
##4.2.1 성적순 자르기
##4.2.2 난수 보정
##4.2.3 순서 섞기
#4.3 return array of product number(product dB)

