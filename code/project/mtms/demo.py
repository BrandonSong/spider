import re
import json


with open("./ms.html", "r", encoding="utf-8") as f:
    data = f.read()
#
# # print(data)
#
ret = re.findall("window._appState = (.*);</script>", data)[0]

json_data = json.loads(ret)



cateList = json_data['navBarData']['categoryList']  # 分类信息
areaList = json_data['navBarData']['areaObj']  # 地区信息

for key, areaValue in areaList.items():
    for area in areaValue:
        print(area)

# for cate in cateList[1:]:
#     for key, areaValue in areaList.items():
#         for area in areaValue:
#             limit = 15
#             offset = 0
#
#             if area["name"] != "全部":
#                 while True:
#                     if limit + offset > 1000:
#                         print(cate["name"], area["name"], area['count'])
#                         print("结束")
#                         break
#                     else:
#                         print(cate["name"], area["name"], area['count'])
#                         print("当前第%d条" % offset)
#                         offset += 15







