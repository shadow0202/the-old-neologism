# -*- coding:utf-8 -*-
import time

import re

_author_ = 'lvhm'

import jieba.posseg
import jieba

# line = "一个"
# list = jieba.posseg.cut(line)
# for u in list:
#     print u.word + ":" + u.flag

# seg_list = jieba.posseg.cut("他来到网易杭研大厦。", HMM=True)
# for u in seg_list:
#     print u.word + ":" + u.flag
# t = int(time.time())
# print t

s = u'介样酱紫灌水灌纯净水潜水女子弓虽木油主要是来自于电竞圈玩CSGO的队员们喜欢喝酒发挥不好的时候就把锅甩给酒我可能是喝了假酒后来被引申到各个领域比如大学生期末考试挂科了就甩锅给复习我可能复习了本假书'
for i in jieba.cut(s):
    poss = jieba.posseg.cut(i)
    for u in poss:
        if u.word != i:
            print 1
            break
        else:
            print u.word