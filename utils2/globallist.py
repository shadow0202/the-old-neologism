# -*- coding:utf-8 -*-
import os
import time

# 全局变量，为了根据新闻类目整合各个网站的标题

list_art = []
list_esports = []
list_edu = []
list_movie = []
list_ent = []
list_health = []
list_mil = []
list_money = []
list_news = []
list_tech = []
list_travel = []
list_video = []
list_sport = []

# 词性表：http://blog.csdn.net/kevin_darkelf/article/details/39520881
list_cixing = ["c", "j", "l", "e", "p", "q", "w", "y", "z", "ul", "uj", "uz", "d", "r", "f", "x", "m"]
list_exdict = ["这是","二人","万起","是", "人", "来", "看", "大", "做", "让", "小", "好", "有", "没", "不能", "等", "无", "没有", "住", "吃", "回应", "发现"]

# t = time.strftime("%Y%m%d")
# filepath = "./result/newdict"+str(t) +".txt"
# if os.path.exists(filepath):
#     os.remove(filepath)
# f = open(filepath, "a")
# map_all = {}
