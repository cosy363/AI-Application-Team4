from concurrent.futures import thread
import json
import pymysql
import random
from single_rec import single_comb
from imshow import imshow
import numpy as np

#1.REST API 형식의 유저 요청 들어옴
#json structure
json_string='''{
    "id": 1,
    "username": "Jinkwon",
    "furniture preference": [2,5,9,8],
    "color preference": [2,4,6]
}'''

json_object = json.loads(json_string)

#Manual Input이 True면 json값으로, 아니면 랜덤으로 지정되어 진행
manual_input = False

#inputs: user color, furniture combination
user_preference = {}
user_preference['user_color'] = json_object['color preference']
user_preference['furniture_combination'] = sorted(json_object['furniture preference'])
######TESTCASE FOR MANUAL COMBINATION ASSESSMENT ONLY##############################
if manual_input == False:
    color_rand, furniture_rand = [1,2,3,4,5,6], [1,2,3,4,5,6,7,8,9]

    color_rand = random.sample(color_rand,4)
    furniture_rand = random.sample(furniture_rand,4)

    user_preference['user_color'] = sorted(color_rand)
    user_preference['furniture_combination'] = sorted(furniture_rand)
##################################################################################
print("FURNITURE PREFERENCE: ",str(user_preference['furniture_combination']))
print("COLOR PREFERENCE: ",str(user_preference['user_color']))


# Convert User Color number for array indexing
for i,k in enumerate(user_preference['user_color']):
    user_preference['user_color'][i] -= 1

#2.rearrange furniture combination by 우선도

#3. single rec

##3.1: prime가구


prime_list,second_list,third_list,final_list = [],[],[],[]
# single_rec.py 돌리기
prime_list = single_comb(user_preference,1)
# output: 10 Ps

##3.2: second가구
# single_rec.py for each 10 Ps = 80 PXS
second_list = single_comb(user_preference,2,prime_list)

##3.3: third가구
# single_rec.py for each 80 PXS = 400 PXSXT
third_list = single_comb(user_preference,3,second_list)

#3.4: final가구
# single_rec.py for 400 PXSXT = 800 PXSXTXF
final_list = single_comb(user_preference,4,third_list)

print("Combination Generated!")

#3.5: sum of combination
for i,a in enumerate(final_list):
    for j,b in enumerate(final_list[i]):
        for k,c in enumerate(final_list[i][j]):
            for l,d in enumerate(final_list[i][j][k]):
                sum = 0.
                price_sum = 0
                for m,e in enumerate(final_list[i][j][k][l]):
                    sum += final_list[i][j][k][l][m]['single score']
                    price_sum += final_list[i][j][k][l][m]['Price']
                final_list[i][j][k][l].append(sum)
                final_list[i][j][k][l].append(price_sum)
            
                pri = final_list[i][j][k][l][0]['New_ID']
                sec = final_list[i][j][k][l][1]['New_ID']
                thr = final_list[i][j][k][l][2]['New_ID']
                fin = final_list[i][j][k][l][3]['New_ID']
                sql = "INSERT INTO furniture_DB.combination_log (product_id1, product_id2, product_id3, product_id4, single_score_sum) VALUES (%d, %d, %d, %d, %f)"
                
                #3.6 Send to mysql DB
                conn2, cur2 = None, None
                conn2 = pymysql.connect(host='127.0.0.1',user='root',password='kimjin12',db='furniture_DB',charset='utf8')

                with conn2:
                    with conn2.cursor() as cur2:
                        cur2.execute(sql % (pri,sec,thr,fin,sum))
                        conn2.commit()

print("Price Sum: "+str(final_list[0][0][0][0][5])+ " 원")

#Show Combination as image
# imshow(final_list,final_list[0][0][0][0][5],0,0,0,0)

# output: [P,S,T,F, sum of single_scores of combination]

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

