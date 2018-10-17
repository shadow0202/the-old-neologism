# coding=utf-8
# 加载库
import urllib2
import json
import sys

from utils2 import globallist, utils

reload(sys)
sys.setdefaultencoding('utf8')
import time
from bs4 import BeautifulSoup

def moviedict():
        # 获取所有标签
        url = 'https://movie.douban.com/j/search_tags?type=movie'
        request = urllib2.Request(url=url)
        request.add_header('User-Agent',
                           'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36')
        request.add_header('Cookie',
                           'bid=T49xdwTmZY4; ll="108288"; __yadk_uid=woHE3QgMUL23JoUFUiyuDxMzsfgc5It1; push_noty_num=0; push_doumail_num=0; __utmv=30149280.17471; _vwo_uuid_v2=D9D3712284AFA69C60840BB052A1BB187|5a281aec8be6c06bc612cfecc841a010; ct=y; __utma=30149280.1227353955.1517381502.1521529769.1521534968.19; __utmz=30149280.1521534968.19.16.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.1064529217.1517469969.1521106834.1521535037.7; __utmb=223695111.0.10.1521535037; __utmz=223695111.1521535037.7.6.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1521535037%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Djz5Q6vo50cs3NxdSUtDbwVKCLL_8iWMOYZnYLWM4fZAeQZEU3PWMwECl63LE--rY%26wd%3D%26eqid%3Df4bbea420001ecdb000000035ab0c7f4%22%5D; _pk_id.100001.4cf6=f4c899e363d94597.1517469969.7.1521535037.1521106841.; _pk_ses.100001.4cf6=*; ps=y; __utmc=30149280; __utmt=1; __utmb=30149280.9.6.1521534968; dbcl2="174712879:Icg9kH/qLsI"; ck=kuI4')

        response = urllib2.urlopen(request, timeout=20)
        result = response.read()
        # 加载json为字典
        result = json.loads(result)
        tags = result['tags']
        # 定义一个列表存储电影的基本信息
        movies = []
        # 处理每个tag
        for tag in tags:
            start = 0
            # 不断请求，直到返回结果为空
            while start <= 60:
                # 拼接需要请求的链接，包括标签和开始编号
                url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=' + tag + '&sort=recommend&page_limit=20&page_start=' + str(
                    start)
                # print url
                try:
                    request = urllib2.Request(url=url)
                    request.add_header('User-Agent',
                                       'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36')
                    request.add_header('Cookie',
                                       'bid=T49xdwTmZY4; ll="108288"; __yadk_uid=woHE3QgMUL23JoUFUiyuDxMzsfgc5It1; push_noty_num=0; push_doumail_num=0; __utmv=30149280.17471; _vwo_uuid_v2=D9D3712284AFA69C60840BB052A1BB187|5a281aec8be6c06bc612cfecc841a010; ct=y; __utma=30149280.1227353955.1517381502.1521529769.1521534968.19; __utmz=30149280.1521534968.19.16.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.1064529217.1517469969.1521106834.1521535037.7; __utmb=223695111.0.10.1521535037; __utmz=223695111.1521535037.7.6.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1521535037%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Djz5Q6vo50cs3NxdSUtDbwVKCLL_8iWMOYZnYLWM4fZAeQZEU3PWMwECl63LE--rY%26wd%3D%26eqid%3Df4bbea420001ecdb000000035ab0c7f4%22%5D; _pk_id.100001.4cf6=f4c899e363d94597.1517469969.7.1521535037.1521106841.; _pk_ses.100001.4cf6=*; ps=y; __utmc=30149280; __utmt=1; __utmb=30149280.9.6.1521534968; dbcl2="174712879:Icg9kH/qLsI"; ck=kuI4')

                    response = urllib2.urlopen(request, timeout=20)
                    result = response.read()
                    result = json.loads(result)
                    result = result['subjects']
                except:
                    pass
                if len(result) == 0:
                    break
                # 将每一条数据都加入movies
                for item in result:
                    movies.append(item)
                # 这里需要修改start
                start += 20

        # 看看一共获取了多少电影
        # print len(movies)

        for x in xrange(0, len(movies)):
            url = movies[x]['url']
            request = urllib2.Request(url=url)
            request.add_header('User-Agent',
                               'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36')
            request.add_header('Cookie',
                               'bid=T49xdwTmZY4; ll="108288"; __yadk_uid=woHE3QgMUL23JoUFUiyuDxMzsfgc5It1; push_noty_num=0; push_doumail_num=0; __utmv=30149280.17471; _vwo_uuid_v2=D9D3712284AFA69C60840BB052A1BB187|5a281aec8be6c06bc612cfecc841a010; ct=y; __utma=30149280.1227353955.1517381502.1521529769.1521534968.19; __utmz=30149280.1521534968.19.16.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.1064529217.1517469969.1521106834.1521535037.7; __utmb=223695111.0.10.1521535037; __utmz=223695111.1521535037.7.6.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1521535037%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Djz5Q6vo50cs3NxdSUtDbwVKCLL_8iWMOYZnYLWM4fZAeQZEU3PWMwECl63LE--rY%26wd%3D%26eqid%3Df4bbea420001ecdb000000035ab0c7f4%22%5D; _pk_id.100001.4cf6=f4c899e363d94597.1517469969.7.1521535037.1521106841.; _pk_ses.100001.4cf6=*; ps=y; __utmc=30149280; __utmt=1; __utmb=30149280.9.6.1521534968; dbcl2="174712879:Icg9kH/qLsI"; ck=kuI4')
            response = urllib2.urlopen(request, timeout=20)
            result = response.read()

            # 使用BeautifulSoup解析html
            html = BeautifulSoup(result)
            # 提取电影简介
            # 捕捉异常，有的电影详情页中并没有简介
            try:
                description = html.find_all("span", attrs={"property": "v:summary"})[0].get_text().strip().replace('\n', '')
            except Exception, e:
                # 没有提取到简介，则简介为空
                description = ''
                movies[x]['description'] = description
            print description
            globallist.list_movie.extend(utils.sencol_nt2(description))
            time.sleep(0.5)

