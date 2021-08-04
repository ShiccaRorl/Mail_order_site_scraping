# -*- coding: utf-8 -*-
import re
import urllib3
from bs4 import BeautifulSoup
import certifi

# アクセスするURL
url = "https://www.yahoo.co.jp/"

#httpsの証明書検証を実行している
http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',ca_certs=certifi.where())

#httpsの証明書検証を実行しない
#http = urllib3.PoolManager()

r = http.request('GET',url)

# htmlをBeautifulSoupで扱う
soup = BeautifulSoup(r.data, 'html.parser')

title_tag = soup.title
title     = title_tag.string

# タイトル要素を出力
print (title_tag)

# タイトルを文字列を出力
print (title)

# 全てのaタグ
for atag in soup.find_all("a"):
    print ("ALL : ")
    print (atag.string)
    print (atag.get("href"))

# 全てのaタグ(条件あり)
for ataglimit in soup.find_all("a", attrs={"class": "link", "href": "/link"}):
    print ("Limit : ")
    print (ataglimit.string)
    print (ataglimit.get("href"))

# 正規表現で検索 BタグやBODYタグなどbで始まるタグをすべて取得
for btag in soup.find_all(re.compile("^b")):
    print (btag.string)

# ”link”を含むhref属性を持っているタグをすべて取得
for altag in soup.find_all(href=re.compile("link")):
    print (altag.get("href"))

# タグの中の文字列に"hello"を含むAタグをすべて取得
for hatag in soup.find_all("a", text=re.compile("hello")):
    print (hatag.get("href"))

# cssセレクタを使ったタグの取得
for catag in soup.select('a[href^="http://"]'):
    print (catag.get("href"))