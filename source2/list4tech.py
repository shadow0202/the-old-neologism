# -*- coding:utf-8 -*-
from utils2.download_page import download_json_waitting, download_soup_waitting
import json
import sys
import time
from utils2 import globallist
reload(sys)
sys.setdefaultencoding('utf8')

# 通过unix时间戳进行当前新闻的拉取
t = int(time.time())

# 网易科技
netease_pages = ['','_02']
# 新浪科技
sina_pages = ['1','2']

def techdict():
    for page in netease_pages:
        list_dic = []
        print ("正在获取techdict...")
        url = r'http://tech.163.com/special/00097UHL/tech_datalist' + page + r'.js?callback=data_callback'
        result = download_json_waitting(url,1)
        result = result.replace("data_callback(", '{"data_callback":', 1)[:-1] + "}"
        result = json.loads(result,strict=False)
        result = result["data_callback"]
        for item in result:
            title = item['title']
            url = item['docurl']
            # print title,url
            try:
                soup = download_soup_waitting(url,'gbk',1)
                content = soup.find('div', {'id': 'endText'})
                [s.extract() for s in content(['div', 'style', 'pre', 'script'])]
                # print title, url, content.get_text().strip().replace('\n', '')
                result = title + content.get_text().strip().replace('\n', '')
                list_dic.append(result)
            except:
                print (title + ":" + url + "格式不相符")
        globallist.list_tech.extend(list_dic)


    for page in sina_pages:
        list_dic = []
        print ("正在获取科技最新资讯...")
        url = r'http://feed.mix.sina.com.cn/api/roll/get?pageid=402&lid=2559&num=20&versionNumber=1.2.8&page=' + \
              page + '&encode=utf-8&callback=feedCardJsonpCallback&_=' + str(t)
        result = download_json_waitting(url,1)
        result = result.replace("try{feedCardJsonpCallback(", '', 1)[:-14]
        result = json.loads(result,strict=False)
        items = result["result"]['data']
        for item in items:
            # print item['title'], item['summary'], item['keywords']
            result = item['title'] + item['summary'] + item['keywords']
            # print result
            list_dic.append(result)
        globallist.list_tech.extend(list_dic)
