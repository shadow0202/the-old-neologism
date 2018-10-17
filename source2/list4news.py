# -*- coding:utf-8 -*-
from utils2.download_page import download_json_waitting, download_soup_waitting
import json
import sys
from utils2 import globallist
reload(sys)
sys.setdefaultencoding('utf8')

# 收集标题的list
def newsdict():
    # 国内、国际、社会类新闻
    tags = ['china','society','world']
    for tag in tags:
        list_dic = []
        print ('正在获newsdict...')
        url = r'http://news.cctv.com/' + tag + r'/data/index.json'
        result = download_json_waitting(url,1)
        result = json.loads(result,strict=False)
        result = result['rollData']
        for item in result:
            title = item["title"]
            url = item['url']
            try:
                soup = download_soup_waitting(url,'utf-8',1)
                content = soup.find('div', {'class': 'cnt_bd'})
                # 剔除无关标签
                [s.extract() for s in content(['div', 'script'])]
                # print title, content.get_text().strip().replace('\n', '')
                result = title + content.get_text().strip().replace('\n', '')
                # print result
                list_dic.append(result)
            except:
                print ("格式不相符")
        globallist.list_news.extend(list_dic)