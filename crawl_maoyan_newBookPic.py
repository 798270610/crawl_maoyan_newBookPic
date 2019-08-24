import urllib.request
import re
import os
import requests


def doubanBookCrawler(url):
    headers = {
        "Users-Agent": "Mozilla/5.0(Windows NT6.1; WOW64)AppleWebKit/537.36(KHTML,likeGecko)Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36"
    }
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)
    HTML = response.read().decode("utf-8")
    # with open(r"F:\PycharmProject\Files\bookFile.html","w",encoding="utf-8")as f:
    #     f.write(HTML)
    pat = '<div id="content">(.*?)<div id="footer">'
    book_pat = re.compile(pat, re.S)
    bookList = book_pat.findall(HTML)
    # print(bookList)
    # 新书照片url列表
    pat1 = '<img src="(.*?)"/></a>'
    bookPic_pat = re.compile(pat1,re.S)
    bookPicList = bookPic_pat.findall(str(bookList))
    # print(bookPicList)
    #新书名称列表
    pat2 = '<h2>(.*?)</h2>'
    name_pat = re.compile(pat2, re.S)
    nameList = name_pat.findall(str(bookList))
    # print(nameList)
    pat3 = '>(.*?)</a>'
    bookName_pat = re.compile(pat3, re.S)
    bookNameList = bookName_pat.findall(str(nameList))
    # print(bookNameList)
    # 打包为字典
    book_dic = dict(zip(bookNameList, bookPicList))
    return book_dic


url = "https://book.douban.com/latest?icn=index-latestbook-all"
topath = r"F:\PycharmProject\images\豆瓣新书速递"
book_dic = doubanBookCrawler(url)
for k, v in book_dic.items():
    path = os.path.join(topath, k+".jpg")
    # v:图片url
    # print(v)
    r = requests.get(v)
    with open(path, "wb")as f:
        f.write(r.content)
