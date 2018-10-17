# -*- coding:utf-8 -*-
from utils2.download_page import download_json_waitting
import json
import sys
import urllib2
from utils2 import globallist
reload(sys)
sys.setdefaultencoding('utf8')

# 收集标题的list
def entdict():
    tags = ['index', 'star', 'movie','music']
    url_hotfeed = "https://api.weibo.cn/2/guest/cardlist?gsid=_2AkMu5Br-f8NhqwJRmPAcz2PmZYl_yQ3EieKYuOslJRM3HRl-3T9kqnwvtRWwLB-1C2SEmptvAP1Bfy0s7kgEgw..&uid=1008938494835&wm=3333_2001&i=8bb4ee5&b=1&from=1073193010&checktoken=807ca79ae3fa897b262e3b63c3882698&c=iphone&networktype=wifi&v_p=45&skin=default&s=ee9f63c1&v_f=1&did=eb4621d547f0e7cb9eef4a41403ee866&lang=zh_CN&sflag=1&ua=iPhone9,2__weibo__7.3.1__iphone__os10.3.1&aid=01AhjayctpFPjOzJEmy46JLMop9TgsXKgsxZQYIpcPoBa-nn8.&lon=116.2697240292689&count=20&fid=230584&containerid=230584&uicode=10000011&lat=40.04127809492162&offset=1&max_id=4151604225452173&page=1&moduleID=pagecard"
    # 明星信息流
    url_starfeed = "https://api.weibo.cn/2/guest/cardlist?gsid=_2AkMu5WfMf8NhqwJRmPAcz2PmZYl_yQ3EieKYuZYXJRM3HRl-3T9kqnZftRVqWDRdwTGKDWtA7iBOAX-N3elOcA..&uid=1008938494835&wm=3333_2001&i=8bb4ee5&b=1&from=1073193010&checktoken=807ca79ae3fa897b262e3b63c3882698&c=iphone&networktype=wifi&v_p=45&skin=default&s=ee9f63c1&v_f=1&did=eb4621d547f0e7cb9eef4a41403ee866&lang=zh_CN&sflag=1&ua=iPhone9,2__weibo__7.3.1__iphone__os10.3.1&aid=01AhjayctpFPjOzJEmy46JLMop9TgsXKgsxZQYIpcPoBa-nn8.&lon=116.2697240292689&count=20&fid=230781&containerid=230781&uicode=10000011&lat=40.04127809492162&offset=1&max_id=4140648884038081&page=1&moduleID=pagecard"
    urlcol = []
    urlcol.append(url_hotfeed)
    urlcol.append(url_starfeed)

    list_dic = []

    #  网易娱乐
    for tag in tags:
        print "正在获取entdict..."
        url = r'http://ent.163.com/special/000380VU/newsdata_' + tag + r'.js'
        result = download_json_waitting(url, 1)
        result = result.replace("data_callback(", '{"data_callback":', 1)[:-1] + "}"
        result = json.loads(result)
        items = result["data_callback"]
        for item in items:
            try:
                title = item['title']
                docurl = item['docurl']
                # print title
                list_dic.append(title)
            except:
                pass

    # 微博信息流
    for url in urlcol:
        print ("正在获取微博信息流...")
        response = urllib2.urlopen(url)
        res = response.read()
        res = json.loads(res)
        try:
            list_dict = []
            for cards in res["cards"]:
                # print cards
                if cards["card_type"] == 9:
                    if "text" in cards["mblog"]:
                        # print cards["mblog"]["text"]
                        list_dic.append(cards["mblog"]["text"])
        except KeyError, e:
            print ("no key: " + str(e))

    globallist.list_ent.extend(list_dic)
