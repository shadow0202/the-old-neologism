# -*- coding:utf-8 -*-
import sys
from utils2 import globallist, utils
from utils2.download_page import download_soup_waitting
reload(sys)
sys.setdefaultencoding('utf8')

# 收集标题的list
def traveldict():

    # 景点信息
    # for i in range(5):
    #     print '正在获取旅游资讯...'
    #     list_dic = []
    #     types=["文化古迹","自然风光","公园","古建筑","寺庙","遗址","古镇","陵墓陵园","故居","宗教"] #实际不止这些分组 需要自己补充
    #     for type in types:
    #         url="http://piao.qunar.com/ticket/list.htm?keyword=%E7%83%AD%E9%97%A8%E6%99%AF%E7%82%B9&region=&from=mpl_search_suggest&subject="\
    #             +type+"&page=" + str(i)
    #         soup = download_soup_waitting(url,'utf-8',1)
    #         search_list = soup.find('div', attrs={'id': 'search-list'})
    #         sight_items = search_list.findAll('div', attrs={'class': 'sight_item'})
    #         for sight_item in sight_items:
    #             name = sight_item['data-sight-name']
    #             districts = sight_item['data-districts']
    #             print name + "--" + districts
    #             result = name + districts
    #             print result
    #             list_dic.append(result)
    #     globallist.list_travel.extend(list_dic)


    # 旅游资讯
    urlcol = [r'http://www.cntour2.com/#']
    print ('正在获取traveldict...')
    for url in urlcol:
        list_dic = []
        soup = download_soup_waitting(url, 'utf8', 1)
        # print soup
        try:
            item = soup.find('div', {'class': 'main_l'})
            news_obj = item.find('ul', {'class': 'news'})
            news = news_obj.find_all('li')
            for new in news:
                # print new
                title = new.find('a').get_text()
                href = r'http://www.cntour2.com/' + new.find('a').get('href')
                # print title, href
                content_page = download_soup_waitting(href, 'utf8', 1)
                content_obj = content_page.find('div', {'id': 'content'})
                if content_obj is None:
                    print ("格式不相符")
                else:
                    companybrief = content_obj.get_text().strip()
                    ss = companybrief.encode('utf-8')
                    uu = ss.replace('\n', '')
                    # print title, href, uu
                    result = title + uu
                    list_dic.append(result)
                    # print result
        except:
            print ("got exception")
            # raise
            continue

        globallist.list_travel.extend(list_dic)