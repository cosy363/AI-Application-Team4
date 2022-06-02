from operator import itemgetter
import pymysql
import random

# 어울림 계수는 1점 만점으로

def single_comb(preference,stage,comb_list=[]):
    prime_sort_order = [0,2,4,6,1,5,3,9,7,8]
    second_sort_order = []


    # import prime가구 category dB from mysql
    conn, cur = None, None
    conn = pymysql.connect(host='127.0.0.1',user='root',password='kimjin12',db='furniture_ikea',charset='utf8')
    cur = conn.cursor

    cur.execute("SELECT * FROM furniture_detail WHERE furniture_category1 = '{}'".format(str(preference['furniture_combination'][stage])))

    furn_list =[]
    return_list =[]
    count = 0
    random.shuffle(furn_list)

    if stage == 1:
        #Single REC 돌리기
        for i,product in enumerate(furn_list):
            count += 1
            score = single_rec(product,preference)
            furn_list[i]['single score'] = score
            if count == 500:
                break
        
        #조합 생성
        sorted_dict = sorted(furn_list, key=itemgetter('single score'), reverse=True)
        for j in prime_sort_order:        
            return_list.append(sorted_dict[j])

        return return_list

    elif stage == 2:
    #Single REC 돌리기
    #[p1,p2,p3...]
        second_list = []
        for k,prime in enumerate(comb_list):
            for i,product in enumerate(furn_list):
                count += 1
                score = single_rec(product,preference,prime)
                furn_list[i]['single score'] = score
                if count == 150:
                    break
            #조합 생성
            sorted_dict = sorted(furn_list, key=itemgetter('single score'), reverse=True)
            for j in second_sort_order:        
                second_list.append(sorted_dict[j])

        return return_list

    elif stage == 3:
        return 0

    elif stage == 4:
        return 0


def single_rec(furn,preference,prime={},second={},third={}):
    abs = 0
    rel = 0
    
    #id를 기준으로 생각하자..

    

    #절대적인 가구 추천 계수
    # rating 
    # number of reviews는 linear하게 적용하자

    score = abs + rel

    return score, abs, rel, 
