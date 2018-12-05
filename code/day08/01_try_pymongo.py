# __author__: liqinsong
# data: 2018/11/27
from pymongo import MongoClient

# 实例化client 建立链接
client = MongoClient(host = "127.0.0.1", port = 27017)
collection = client["read_source"]["t251"]

# 插入一条数据
# ret1 = collection.insert({"_id": 10001, "name": "xiaowang", "age": 10})
# print(ret1)

# 插入多条数据
# data_list = [{"name": "read_source{}".format(i)} for i in range(10)]
# ret2 = collection.insert_many(data_list)
# print(ret2)

# 查询一个记录
# t = collection.find_one({"name": "xiaowang"})
# print(t)


