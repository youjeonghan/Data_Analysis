import json
from pymongo import MongoClient
import timeit
from pprint import pprint

start_time = timeit.default_timer()  # 시작 시간 체크
my_client = MongoClient("mongodb://localhost:27017/")
mydb = my_client["project"]  # 몽고db명
mycol = mydb["test_data"]  # 해당 db collection명


for raw_data in range(0, 1):
    """전체 data 삽입"""
    suffix = f"{raw_data}".zfill(2)
    with open(f"raw_data\\data_0000000000{suffix}", "r") as f:  # 기본 로우데이터 네임
        data_list = []
        for line in f:
            temp_json = json.loads(line)  # list 안에 각각의 json 담기
            for item in temp_json["event_params"] + temp_json["user_properties"]:
                """item의 형태
                {'key': ~,
                'value': ~}
                """
                if item["key"] == "ad_id":
                    temp_json[item["key"]] = item["value"]["string_value"]
                else:
                    temp_json[item["key"]] = item["value"]

            del temp_json["event_params"]
            del temp_json["user_properties"]
            data_list.append(temp_json)

        mycol.insert_many(data_list)

        print(
            f"raw_data\\data_0000000000{suffix} success 시작 후 {timeit.default_timer() - start_time}초 경과"
        )
