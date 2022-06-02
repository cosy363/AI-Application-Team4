from cmath import sin
import json
import pymysql
from single_rec import single_rec,single_comb


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
user_preference['furniture_combination'] = json_object['furniture preference'].sorted

#2.rearrange furniture combination by 우선도

#3. single rec

##3.1: prime가구


prime_list,second_list,third_list,final_list = [],[],[],[]
# single_rec.py 돌리기
prime_list = single_comb(user_preference,1)
# output: 10 Ps

##3.2: second가구 
#[p1,p2p3...]
second_list = single_comb(user_preference,2,prime_list)

third_list = single_comb(user_preference,3,second_list)

final_list = single_comb(user_preference,4,third_list)


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

