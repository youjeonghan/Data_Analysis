import pandas as pd
import json
from pandas import json_normalize
from pymongo import MongoClient

my_client = MongoClient("mongodb://localhost:27017/")
mydb = my_client["testdb"]
mycol = mydb["check"]

li = []
with open("data\\raw_data-20210315T141116Z-001\\data_000000000015.json", "r") as f:
    for line in f:
        li.append(json.loads(line))  # list 안에 각각의 json 담기

x = mycol.insert_many(li)
print(x.inserted_ids)
