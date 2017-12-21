# coding=UTF-8
import requests
url = 'https://www.baidu.com'


def req_get(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "发生异常"


print req_get(url)