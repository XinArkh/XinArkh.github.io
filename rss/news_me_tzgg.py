#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import datetime
import PyRSS2Gen
import requests
from bs4 import BeautifulSoup
import re


titles = []
links = []
descriptions = []
pubDates = []
prefix = 'http://me.zju.edu.cn'


def get_article(link):
    try:
        r = requests.get(link)
        bsObj = BeautifulSoup(r.content.decode('utf-8', 'ignore'))
        article = bsObj.find('div', {'class':'wp_articlecontent'}).text
    except:
        article = ''
    article = re.sub('\xa0|\u2003', ' ', article)
    return article


def rssgen():
    items = []
    for i in range(len(titles)):
        items.append(PyRSS2Gen.RSSItem(
                        title = titles[i],
                        link = links[i],
                        description = descriptions[i],
                        pubDate = pubDates[i])
        )
    rss = PyRSS2Gen.RSS2(title = "浙江大学机械工程学院-通知公告",
            link = "http://me.zju.edu.cn/meoffice/tzgg/list.htm",
            description = "浙江大学机械工程学院-通知公告",
            lastBuildDate = datetime.datetime.now(),
            items = items
            )
    rss.write_xml(open("news_me_tzgg.xml", "w"), 'gbk')


def me_tzgg():
    r = requests.get('http://me.zju.edu.cn/meoffice/tzgg/list.htm')
    bsObj = BeautifulSoup(r.content.decode('utf-8', 'ignore'))
    newsBunch = bsObj.find('div', {'id':'wp_news_w9'}).ul.findAll('li')
    for news in newsBunch:
        child1, child2 = news.children
        titles.append(child1.text)
        if child1.a.attrs['href'][0] == '/':
            fullLink = prefix + child1.a.attrs['href']
        else:
            fullLink = child1.a.attrs['href']
        links.append(fullLink)
        descriptions.append(get_article(fullLink))
        year, month, day = [int(a) for a in child2.text.split('-')]
        pubDates.append(datetime.datetime(year, month, day))
    rssgen()


if __name__ == '__main__':
    me_tzgg()