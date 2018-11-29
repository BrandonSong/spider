# __author__: liqinsong
# data: 2018/11/27
from pymongo import MongoClient

client = MongoClient()

collection = client["test"]["t252"]

# 插入一千条数据
# data_list = [{"_id": i, "name": "py{}".format(i)} for i in range(1000)]
#
# collection.insert_many(data_list)

# 查询_id是100的倍数的记录,并输姓名
ret = collection.find()

data_list = list(ret)

data_list = [i for i in data_list if i["_id"] % 100 == 0 and i["_id"] != 0]

print(data_list)


