import re
import json
from ast import literal_eval


with open("./ms.html", "r", encoding="utf-8") as f:
    data = f.read()

# print(data)

ret = re.findall("window._appState = (.*);</script>", data)[0]

json_data = json.loads(ret)

print(json_data['navBarData']['categoryList'])  # 分类信息
print(json_data['areaList'])  # 地区信息
print(json_data['uuid'])
