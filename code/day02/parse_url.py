import requests
from retrying import retry


headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Mobile Safari/537.36",
    # "Host": "m.douban.com",
    "Referer": "https://m.douban.com/movie/nowintheater?loc_id=108288"
}


@retry(stop_max_attempt_number=3)
def _parse_url(url, method, data):
    if method == "POST":
        response = requests.post(url, data=data, headers=headers)
    else:
        response = requests.get(url, headers=headers)
    print(response.status_code)
    return response.content.decode()


def parse_url(url, method="GET", data=None):
    try:
        html_str = _parse_url(url, method, data,)
    except:
        html_str = None

    return html_str

