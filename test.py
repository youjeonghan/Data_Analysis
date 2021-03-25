import pandas as pd
import json
from pandas import json_normalize
from pymongo import MongoClient
import timeit
from pprint import pprint

start_time = timeit.default_timer()  # 시작 시간 체크
my_client = MongoClient("mongodb://localhost:27017/")
mydb = my_client["project"] # 몽고db명
mycol = mydb["All_data"]    # 해당 db collection명

# 전체 data 삽입
for data_num in range(0, 1): # 두번째 인자 100 넣을시 0~99 로우데이터 모두 읽어옴
    st = f"{data_num}".zfill(2)
    with open(f"raw_data\\data_0000000000{st}", "r") as f:  # 기본 로우데이터 네임
        for line in f:
            temp_json = (json.loads(line))  # list 안에 각각의 json 담기

            """
            temp_json을 사용하여 ad_id를 기준으로 데이터를 
            만들어 삽입하는 코드가들어갈 섹션
            """
            pprint(temp_json)
            event_params = [temp_json[event_params][key],temp_json[event_params][value]]
            user_properties = [temp_json[event_params][key],temp_json[event_params][value]]
            del temp_json["event_params"]
            del temp_json["user_properties"]
            ad_id = None
            new_json[temp_json] = 
            
            break
            mycol.insert(li)   # 몽고db 삽입


        print(
            f"raw_data\\data_0000000000{st} success 시작 후 {timeit.default_timer() - start_time}초 경과"
        )
