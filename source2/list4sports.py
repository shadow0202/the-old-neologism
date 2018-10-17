# -*- coding:utf-8 -*-
import json
from utils2 import globallist, utils
import sys
from utils2.download_page import download_json_waitting, download_soup_waitting
reload(sys)
sys.setdefaultencoding('utf8')

urlcol = ['http://sports.163.com/special/000587PK/newsdata_nba_index.js?callback=data_callback',
'http://sports.163.com/special/000587PN/newsdata_world_index.js?callback=data_callback',
'http://sports.163.com/special/000587PM/newsdata_china_index.js?callback=data_callback',
'http://sports.163.com/special/000587PQ/newsdata_allsports_index.js?callback=data_callback']

# 收集标题的list
def sportsdict():
    # NBA && CBA & 国足 & 国际足球 & 综合
    for url in urlcol:
        print ('正在获取sportsdict...')
        list_dic = []
        result = download_json_waitting(url, 1)
        result = result.replace("data_callback(", '{"data_callback":', 1)[:-1] + "}"
        result = json.loads(result,strict=False)
        items = result['data_callback']
        for item in items:
            title = item['title']
            docurl = item['docurl']
            # print title, docurl
            soup = download_soup_waitting(docurl, 'gbk', 1)
            try:
                post = soup.find('div', id="endText")
                if post is None:
                    print ("格式不相符")
                else:
                    companybrief = post.get_text().strip()
                    uu = companybrief.replace('\n', '')
                    # print uu
                    list_dic.append(uu)
            except:
                print ("链接异常，跳往下一链接")
        globallist.list_sport.extend(list_dic)


