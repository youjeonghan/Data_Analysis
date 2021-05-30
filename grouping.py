import json
from pymongo import MongoClient
import timeit
from pprint import pprint
from collections import defaultdict

start_time = timeit.default_timer()  # 시작 시간 체크
my_client = MongoClient("mongodb://localhost:27017/")
mydb = my_client["project"]
mycol = mydb["test_data"]
target_col = mydb["clean_data"]

"""
"""
group_ad = defaultdict(
    lambda: {
        "ads": [],
        "stage_start": [],
        "stage_end": [],
        "draw_start": [],
        "draw_end": [],
        "asset": [],
        "play_start": [],
        "play_end": [],
        "activity": [],
        "screen_view": [],
        "session_start": [],
        "tutorial": [],
        "item": [],
        "cross": [],
        "purchase": [],
        "user_engagement": [],
        "app_update": [],
        "app_remove": [],
        "os_update": [],
        "app_clear_data": [],
        "firebase_campaign": [],
    }
)

for item in mycol.find({}):
    # pprint(item)
    if item.get("ad_id") != None:
        group_ad[item["ad_id"]][item["event_name"]].append(item)


_list = []
for key, value in group_ad.items():
    _list.append({f"{key}": value})

target_col.insert_many(_list)
print(f"raw_data\\data_0000000000{suffix} success 시작 후 {timeit.default_timer() - start_time}초 경과")
