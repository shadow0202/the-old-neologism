# -*- coding:utf-8 -*-
import json
import sys
from utils2 import globallist, utils
from utils2.download_page import download_json_waitting, download_soup_waitting
reload(sys)
sys.setdefaultencoding('utf8')
type = sys.getdefaultencoding()

# 财经网,网易财经
url_col=["http://money.163.com/special/002557S5/newsdata_idx_index.js?callback=data_callback",
"http://money.163.com/special/002557S5/newsdata_idx_stock.js?callback=data_callback",
'http://jingji.cctv.com/data/index.json']

# 收集标题的list
def moneydict():
    for url in url_col:
        list_dic = []
        print ('正在获取moneydict...')
        result = download_json_waitting(url,1)
        if url == 'http://jingji.cctv.com/data/index.json':
            result = json.loads(result,strict=False)
            result = result['rollData']
            for item in result:
                title = item['title']
                url = item['url']
                soup = download_soup_waitting(url,'utf-8',1)
                try:
                    content = soup.find('div', {'class': 'cnt_bd'})
                    # 剔除无关标签
                    [s.extract() for s in content(['div', 'style', 'pre', 'script'])]
                    result = title + content.get_text().strip().replace('\n', '')
                    # print result
                    list_dic.append(result)
                except:
                    print ('格式不相符')
        else:
            try:
                result = result.replace("data_callback(", '{"data_callback":', 1)[:-1] + "}"
                result = json.loads(result,strict=False)
                result = result["data_callback"]
                for item in result:
                    title = item['title']
                    url = item['docurl']
                    # print url
                    soup = download_soup_waitting(url,'gbk',1)
                    try:
                        content = soup.find('div', {'id': 'endText'})
                        [s.extract() for s in content(['div', 'style', 'pre', 'script'])]
                        result = title + content.get_text().strip().replace('\n', '')
                        # print result
                        list_dic.append(result)
                    except:
                        print ('格式不相符')
            except:
                pass

        globallist.list_money.extend(list_dic)

