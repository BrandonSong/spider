# __author__: liqinsong
# data: 2018/12/11

import requests
from lxml import etree

url = "https://movie.douban.com/cinema/nowplaying/shanghai/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36"
}


resp = requests.get(url, headers=headers)

html = etree.HTML(resp.content.decode())

li_list = html.xpath("//div[@id='nowplaying']//ul[@class='lists']/li")

for li in li_list:
    movie_name = li.xpath("./@data-title")[0]
    movie_score = li.xpath("./@data-score")[0]
    item = {
        "movie_name": movie_name,
        "movie_score": movie_score
    }
    print(item)



