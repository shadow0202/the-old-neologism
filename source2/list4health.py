# -*- coding:utf-8 -*-
import re
import json
import sys
from utils2 import globallist
from utils2.download_page import download_json_waitting
reload(sys)
sys.setdefaultencoding('utf8')


urlcol=[
'http://www.cn-healthcare.com/api/article/articlelist?data={%22start%22:%221%22,%22size%22:%2210%22,%22arctype%22:%223%22}',
'http://www.cn-healthcare.com/api/article/articlelist?data={%22start%22:%221%22,%22size%22:%2210%22,%22arctype%22:%2243%22}',
'http://www.cn-healthcare.com/api/article/articlelist?data={%22start%22:%221%22,%22size%22:%2210%22,%22arctype%22:%226%22}',
'http://www.cn-healthcare.com/api/article/articlelist?data={%22start%22:%221%22,%22size%22:%2210%22,%22arctype%22:%224%22}',
'http://www.cn-healthcare.com/api/article/articlelist?data={%22start%22:%221%22,%22size%22:%2210%22,%22arctype%22:%2250%22}',
'http://www.cn-healthcare.com/api/article/articlelist?data={%22start%22:%221%22,%22size%22:%2210%22,%22arctype%22:%2254%22}',
'http://www.cn-healthcare.com/api/article/articlelist?data={%22start%22:%221%22,%22size%22:%2210%22,%22arctype%22:%2251%22}',
'http://www.cn-healthcare.com/api/article/articlelist?data={%22start%22:%221%22,%22size%22:%2210%22,%22arctype%22:%2216%22}',
'http://www.cn-healthcare.com/api/article/articlelist?data={%22start%22:%221%22,%22size%22:%2210%22,%22arctype%22:%2252%22}'
]

# 收集标题的list
def healthdict():
    for url in urlcol:
        list_dic = []
        print ('正在获取healthdict....')
        result = download_json_waitting(url,1)
        result = json.loads(result,strict=False)
        items = result["data"]
        for item in items:
            try:
                title = item['title']
                content = item['content']
                r = re.compile(r'\<.*?\>')
                content = r.sub('', content)
                # print title + '-----' + content
                list_dic.append(title + content)
            except:
                title = item['title']
                description = item['description']
                # print title + "--" + description
                list_dic.append(title + description)

        globallist.list_health.extend(list_dic)
