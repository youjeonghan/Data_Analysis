import os

extensions1 = os.path.splitext("raw_data\\data_000000000000")[1]
extensions2 = os.path.splitext("raw_data\\data_000000000000.json")[1]

print(extensions2, type(extensions2))
if extensions1 == "":
    print(extensions1)

if extensions1 == ".json":
    print(extensions2)