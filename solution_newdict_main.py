# -*- coding:utf-8 -*-
_author_ = 'lvhm'

import time

from utils2 import mergesort, globallist

# 设置每个类目的新词提取个数，如果需要全部新词，填'all'
num = 20

# print "\n###################【NEWDICT:" + time.strftime('%Y-%m-%d %H:%M:%S',
#                                                        time.localtime(time.time())) + "】######################"
# globallist.f.writelines("\n###################【NEWDICT:" + time.strftime('%Y-%m-%d %H:%M:%S',
#                                                                          time.localtime(time.time())) + "】######################")
# print "##########【TOP】教育、娱乐、体育、军事、新闻、电影、旅游、科技、运动、电竞、健康、经济###############"
# globallist.f.writelines("\n##########【TOP】教育、娱乐、体育、军事、新闻、电影、旅游、科技、运动、电竞、健康、经济###############\n")


mergesort.mergenews("newdict", num)

