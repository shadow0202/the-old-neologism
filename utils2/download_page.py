# -*- coding:utf-8 -*-
import urllib2
import chardet
import requests
import time
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf8')
type = sys.getdefaultencoding()

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}

def download_json_waitting(url,num):
    try:
        response= requests.get(url,headers=headers,allow_redirects=False,timeout=5)
        if response.status_code==200:
            request = urllib2.Request(url=url, headers=headers)
            response = urllib2.urlopen(request, timeout=20)
            result = response.read()
            chardit = chardet.detect(result)
            result = result.decode(chardit['encoding'], 'ignore')
            return result
        else:
            # 等待五秒，链接异常直接跳往下一链接
            if num < 5 :
                time.sleep(1)
                print("等待ing")
                return download_soup_waitting(url,num + 1)
            else:
                print ('链接异常')
    except:
        return ""

def download_soup_waitting(url,coding,num):
    try:
        response= requests.get(url,headers=headers,allow_redirects=False,timeout=5)
        if response.status_code==200:
            html=response.content
            html=html.decode(coding)
            soup = BeautifulSoup(html, "html.parser")
            return soup
        else:
            # 等待五秒，链接异常直接跳往下一链接
            if num < 5 :
                time.sleep(1)
                print("等待ing")
                return download_soup_waitting(url,coding,num + 1)
            else:
                print ('链接异常')
    except:
        return ""