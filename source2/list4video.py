# -*- coding:utf-8 -*-
import StringIO
import gzip
import chardet
import re
from bs4 import BeautifulSoup
import sys
import time
import urllib2
reload(sys)
sys.setdefaultencoding('utf8')
type = sys.getdefaultencoding()

# 通过unix时间戳进行当前新闻的拉取
t = int(time.time())
urlcol = []


# 爱奇艺\综艺
url_iqiyi_fun = 'http://www.iqiyi.com/zongyi/'
# 百度风云榜\综艺
url_baidu_fun = "http://top.baidu.com/category?c=3&fr=topcategory_c3"
# 搜狐视频\综艺
url_souhu_fun = "http://tv.sohu.com/show/"

urlcol.append(url_iqiyi_fun)
urlcol.append(url_baidu_fun)
urlcol.append(url_souhu_fun)


# 收集标题的list
def videodict():
    for url in urlcol:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
            req = urllib2.Request(url, headers=headers)
            response = urllib2.urlopen(req)
            isGzip = response.info().get('Content-Encoding')
            if isGzip == 'gzip':
                buf = StringIO.StringIO(response.read())
                f = gzip.GzipFile(fileobj=buf)
                res = f.read()
            else:
                res = response.read()
            response.close()

            chardit = chardet.detect(res)

            res = res.decode(chardit['encoding'], 'ignore').encode(type)
            soup = BeautifulSoup(res, 'lxml')
            [script.extract() for script in soup.findAll('script')]
            [style.extract() for style in soup.findAll('style')]
            reg1 = re.compile("<[^>]*>")
            content = reg1.sub('', soup.prettify())
            data = content.strip().replace(' ', '').replace('\n', '').replace('\t', '').replace('\r', '').strip()
            # print data

            globallist.list_video.extend(utils.sencol_nt2(data))
            print globallist.list_video

