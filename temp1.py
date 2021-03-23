from pymongo import MongoClient
from pprint import pprint
import pandas as pd

my_client = MongoClient("mongodb://localhost:27017/")
mydb = my_client["project"]
mycol = mydb["All_data"]

myquery = {"event_name": "ads"}
result_see = {"_id": False, "event_name": True, "event_params": True}
_list = mycol.find(myquery, result_see).limit(3)

# for i in _list:
#     pprint(i)

temp = pd.DataFrame(_list)
pprint(temp)
print("exit")