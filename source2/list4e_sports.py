# -*- coding:utf-8 -*-
import json
import sys
from utils2 import globallist
from utils2.download_page import download_soup_waitting, download_json_waitting
reload(sys)
sys.setdefaultencoding('utf8')

def esportsdict():
    for i in range(1,10):
        print ('正在获取esportsdict....')
        list_dic = []
        url = 'http://www.dadianjing.cn/index.php?m=Index&a=xhrList&cid=1&page='+str(i)
        result = download_json_waitting(url,1)
        try:
            result = json.loads(result,strict=False)
            items = result["data"]["list"]
            for item in items:
                title = item['title']
                summary = item['summary']
                # print title + "---" + summary
                list_dic.append(title + summary)

            globallist.list_esports.extend(list_dic)

        except:
            print ("链接异常")


