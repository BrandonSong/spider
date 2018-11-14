import json
from parse_url import parse_url
from pprint import pprint


url = "https://m.douban.com/rexxar/api/v2/subject_collection/movie_showing/items?start=0&count=18&loc_id=108288"

html_str = parse_url(url)

data = json.loads(html_str)

pprint(data)
