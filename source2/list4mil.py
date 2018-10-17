# -*- coding:utf-8 -*-
import re
from utils2.download_page import download_json_waitting, download_soup_waitting
import json
import sys
import time
from utils2 import globallist
reload(sys)
sys.setdefaultencoding('utf8')

# 通过unix时间戳进行当前新闻的拉取
t = int(time.time())

# 收集标题的list
def mildict():
    for i in range(1,3):
        list_dic = []
        print ('正在获mildict...')
        url = 'http://platform.sina.com.cn/news/news_list?app_key=2872801998&channel=mil&cat_1=jssd&show_all=0&show_cat=1&show_ext=1&tag=1&format=json&page='+ str(i) +\
              '&show_num=10'
        result = download_json_waitting(url,1)
        result = json.loads(result,strict=False)
        items = result["result"]["data"]
        for item in items:
            title = item['title']
            url = item['url']
            try:
                soup = download_soup_waitting(url, 'utf-8', 1)
                content = soup.find('div', {'id': 'article'})
                [s.extract() for s in content(['div', 'style', 'pre', 'script'])]
                content = content.get_text().strip().replace('\n', '')
                # print title + "---" + url + "----" + content
                list_dic.append(title + content)
            except:
                print (title + ":" + url + "格式不相符")

        globallist.list_mil.extend(list_dic)