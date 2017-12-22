# coding=UTF-8
import requests
from bs4 import BeautifulSoup
import bs4
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


def get_html(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def fill_ulist(ulist, html):
    soup = BeautifulSoup(html, 'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            # 所有的td标签
            tds = tr('td')
            rank = tr.td.contents[0]
            ulist.append([rank, tds[1].string, tds[3].string])


def print_rand(ulist, ranknum):
    tplt = "{0:^10}\t{1:^10}\t{2:^10}"
    print(tplt.format("排名", "学校名称", "总分"))
    for i in range(ranknum):
        u = ulist[i]
        print(tplt.format(u[0], u[1], u[2]))


def main():
    url = "http://www.zuihaodaxue.com/zuihaodaxuepaiming2017.html"
    randlist = []
    html = get_html(url)
    fill_ulist(randlist, html)
    print_rand(randlist, 20)

main()