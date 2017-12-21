# coding=UTF-8
import requests
url = 'http://www.baidu.com/s'


def req_get(url):
    try:
        kv = {'wd': 'python'}
        r = requests.get(url, params=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print r.url
        return r.text
    except:
        return "发生异常"


print req_get(url)