# coding=UTF-8
import requests
import os
url = 'http://www.hishop.com.cn/uploads/150914/21678-150914112244436.jpg'
root = "L://pics//"
path = root + url.split('/')[-1]


def req_get(url):
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r = requests.get(url)
            r.raise_for_status()
            with open(path, 'wb') as f:
                f.write(r.content)
                f.close()
                return "文件保存成功"
    except:
        return "文件保存失败"


print req_get(url)
