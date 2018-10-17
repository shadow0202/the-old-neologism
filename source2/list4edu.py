# -*- coding:utf-8 -*-
import json
import sys
from utils2 import globallist
from utils2.download_page import download_json_waitting, download_soup_waitting
reload(sys)
sys.setdefaultencoding('utf8')

urlcol = [
'http://edu.163.com/special/002987KB/newsdata_edu_hot',
'http://edu.163.com/special/002987KB/newsdata_edu_daxue',
'http://edu.163.com/special/002987KB/newsdata_edu_gaokao',]

# 收集标题的list
def edudict():
    nums = ['']
    for url in urlcol:
        for num in nums:
            print ('正在获取edudict....')
            list_dic = []
            page_url = url + num + '.js'
            print url, page_url
            result = download_json_waitting(page_url,1)
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
                        print "格式不相符"
                    else:
                        companybrief = post.get_text().strip()
                        ss = companybrief.encode('utf-8')
                        uu = ss.replace('\n', '')
                        # print uu
                        list_dic.append(uu)
                except:
                    print ("链接异常，跳往下一链接")

            globallist.list_edu.extend(list_dic)