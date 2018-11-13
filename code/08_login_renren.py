import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"
}

cookies = ""

cookies = {i.split("=")[0]: i.split("=")[1] for i in cookies.split("; ")}

