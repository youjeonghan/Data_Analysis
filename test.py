import pandas as pd
import json
from pandas import json_normalize
from pymongo import MongoClient
import timeit

start_time = timeit.default_timer()  # 시작 시간 체크
my_client = MongoClient("mongodb://localhost:27017/")
mydb = my_client["testdb"]
mycol = mydb["check"]

for i in range(1, 100):
    li = []
    st = f"{i}".zfill(2)
    with open(f"raw_data\\data_0000000000{st}", "r") as f:

        for line in f:
            li.append(json.loads(line))  # list 안에 각각의 json 담기
        mycol.insert_many(li)
        print(
            f"raw_data\\data_0000000000{st} success 시작 후 {timeit.default_timer() - start_time}초 경과"
        )
