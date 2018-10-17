# -*- coding:utf-8 -*-
from utils2 import mysqlhelp

_author_ = 'lvhm'

import json
import os
import re
import time
import urllib2
import jieba
import jieba.posseg
import globallist

# f = open(globallist.filepath, "a")
mh = mysqlhelp.MysqlHelp()


# 纪录单词频率
def record(l):
    list_record = []
    list_set = set(l)
    for item in list_set:
        # print("the %s has found %d" % (item, l.count(item)))
        list_record.append(item + '\t' + str(l.count(item)))
    return list_record


# 查询频率top N
def topN(l, n):
    num = 0
    l_api = []
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            a = str(l[i]).split("\t")
            b = str(l[j]).split("\t")
            if int(a[1]) < int(b[1]):
                tmp = l[i]
                l[i] = l[j]
                l[j] = tmp
        num += 1
        # 找到前N个，后续不再排序
        if num == n:
            l_api = json.dumps(l[0:num]).decode("unicode-escape")
            print "top" + str(num) + ":" + l_api
            # globallist.f.writelines("\ntop" + str(num) + ":" + l_api)
            return l_api
    # 没有那么多的topN,有几个返回几个
    if num < n:
        l_api = json.dumps(l[0:num]).decode("unicode-escape")
        print "top" + str(num) + ":" + l_api
        # globallist.f.writelines("\ntop" + str(num) + ":" + l_api)
        return l_api
    if n == "all":
        l_api = json.dumps(l[0:num]).decode("unicode-escape")
        print "all dict return【 " + str(num) + "】:" + l_api
        # globallist.f.writelines("\nall dict return【 " + str(num) + "】:" + l_api)
    return l_api



# 发请求验证
def jsonapi(l,field ):
    l = json.loads(l.encode("unicode-escape"))
    for element in l:
        # i = element[0:-2]
        i = str(element).split("\t")
        print "key:【" + i[0] + "】\tnum:【" + i[1] + "】"
        # 插入新数据
        sql = "INSERT INTO show_newwords_newwords(new_word,counts,types) VALUES('%s',%d,'%s')" %(i[0],int(i[1]),field)
        mh.insert(sql=sql)
        # globallist.f.writelines("\nkey:【" + i[0] + "】\tnum:【" + i[1] + "】")
        # url_ver = "http://k12yuwen.corp.youdao.com/k12yuwen/edit/getVal.v?dictType=hh&key=" + str(
        print "dict returns:" + getRes(i[0])
        # globallist.f.writelines("\ndict returns:" + getRes(i[0]))
        res = json.loads(getRes(i[0]))
        if "val" in res:
            print "Exist:【true】\n"
            # globallist.f.writelines("\nExist:【true】\n")
        else:
            print "Exist:【false】\n"
            # globallist.f.writelines("\nExist:【false】\n")
            # filename = mergenewdict()
            # f = open(filename, "a")
            # f.writelines(i[0] + "\t" + i[1] + "\n")
            # f.close()


# 除了头条，拿到完整标题
def sencol_nt(f, res):
    list_sen = []
    for o in res[f]:
        # print title
        if "title" in o:
            list_sen.append(o["title"])
    return list_sen

def sencol_nt2(res):
    list_sen = []
    list_sen.append(res)
    return list_sen

# 头条拿到完整标题
def sencol_toutiao(f, res):
    list_sen = []
    for o in res[f]:
        o = json.loads(o["content"])
        if "title" in o:
            list_sen.append(o["title"])
    return list_sen


def getStopWords():
    stop_dic = {}
    sql = "select stop_word from show_newwords_stop_list"
    res = mh.selectall(sql=sql)
    for row in res:
        fname = row[0]
        stop_dic[fname] = 1
    return stop_dic


def getRes(word):
    url_ver = "http://k12yuwen.corp.youdao.com/k12yuwen/edit/getVal.v?dictType=hh&key=" + word
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}
    maxTryNum=10
    res = ""
    for tries in range(maxTryNum):
        try:
            request = urllib2.Request(url=url_ver, headers=headers)
            request.add_header('Cookie',
                               'OUTFOX_SEARCH_USER_ID=170305599@220.181.102.181; OUTFOX_SEARCH_USER_ID_NCOO=1552007743.8650935; _ga=GA1.2.345142933.1517627252; _ntes_nnid=41bf96b62d2ca64581afa43369d3f1a6,1518332076685; P_INFO=shadow_workspace@126.com|1519706200|0|other|00&99|heb&1518618608&g83_client#bej&null#10#0#0|&0||shadow_workspace@126.com; DICT_PERS=v2|urstoken||DICT||web||-1||1519966774953||220.181.102.181||shadow_workspace@126.com||UfRfTFnMgFRYEh4gF6MlE0gKOLqKh4OW0lW64T4n4Um06yPMq4kfPuReBhMO5P4wz0Ym0MpK0LeFRTzOLQShHJBR; __guard_cookie__=36a9f167b4c743c2e3773870abab86b7|1519979971318|I0ZyaSBNYXIgMDIgMTY6Mzk6MzEgQ1NUIDIwMTgKdmVyc2lvbj0wCm5pY2tuYW1lPWh1eHcKZW1h_aWw9aHV4d0ByZC5uZXRlYXNlLmNvbQpwPTEKZ3JvdXA9MQo=; DICT_SESS=v2|P57TaH0cDmqZhHw4RfJBReunLTShHTB0gFn4wFPLpFRwyRfk5RHl50kmhMOGn4g40km6LTKh4ey0T40LquhLpu0J4k4ey0MQuR; DICT_LOGIN=5||1520928642776; _gid=GA1.2.316774567.1521182514')
            # re
            response = urllib2.urlopen(request)
            res = response.read()
            break
        except:
            if tries <(maxTryNum-1):
                continue
            else:
                print ("Has tried %d times to access url %s, all failed!",maxTryNum,url_ver)
                break

    return res


# 过滤、分词
def filter(list_raw, type,stop_Dic):
    list_dict = []
    list_new = []
    for raw in list_raw:
        # print "_______________________________________________________________________________"
        # print raw
        # 过滤微博信息流中的表情
        raw = re.sub(r'\[.*?\]', "", raw.decode('utf-8', 'ignore'))
        # 过滤标点符号
        line = re.sub(r"[\s：；:，》《><，、，“”·！？？+-.!\/！_,$%^*(+\"\')]+|[+——()?【】\“\”！，。？、~@#￥%……&*（）]+'".decode("utf8"),"".decode("utf8"),raw.decode('utf-8', 'ignore'))
        wordList = list(jieba.cut(line))  # 用结巴分词，对每行内容进行分词
        for word in wordList:
            # print word
            poss = jieba.posseg.cut(word)
            for u in poss:
                # if u.word != word and stop_List.has_key(word) == False:
                #     list_new.append(word)
                #     # list_dict.append(word)
                #     break
                # else:
                if u.flag not in globallist.list_cixing and stop_Dic.has_key(word.encode('utf-8')) == False:
                    if getRes(u.word) != "":
                        if "val" in json.loads(getRes(u.word)):
                            list_dict.append(u.word)
                        else:
                            list_new.append(u.word)
    if type == "hotdict":
        return list_dict
    elif type == "newdict":
        # print list_new
        return list_new
        # return list_dict


def sort(list_s, N, type,field,stop_List):
    # 过滤、分词
    print (type+"正在分词....")
    list_dict = filter(list_s, type,stop_List)
    # 去重
    # for i in list_dict:
    #     print i
    list_dict = record(list_dict)
    if len(list_dict) == 0:
        print ("no new dict!")
        return list_dict
    # topN
    list_dict = topN(list_dict, N)
    # 发请求
    jsonapi(str(list_dict),field)
    return list_dict


# 转中文格式，目前没用
def utf8convert(map_dict):
    # unicode->中文
    map_dict = json.dumps(map_dict)
    map_dict = map_dict.decode("unicode-escape")
    return map_dict


# 新词统计文本,如果存在文件就用之前的，如果不存在就新建
# ne为boolean，true时如果有已经存在的文件就不新建文件，false需要新建文件
def mergenewdict(ne=True):
    files = []
    for root, dir, file in os.walk("./"):
        if root == "./":
            files = file
            break
    # b = False
    # 匹配以newdict开头的文件
    if ne:
        for i in files:
            if re.match("newdict", i) != None:
                # b = True
                return i
    # 如果不存在文件就新建
    if not ne:
        t = time.strftime("%Y%m%d")
        newpath = "newdict" + t + ".txt"
        return newpath


def total(filename):
    f = open(filename, "r")
    new = {}
    while (1):
        s = f.readline()
        if not s:
            f.close()
            break
        d = s.split("\t")
        # 如果新词不存在就添加，如果存在就累加
        if d[0] in new.keys():
            num = new.get(d[0]) + int(d[1])
            new[d[0]] = num
        else:
            new.setdefault(d[0], int(d[1]))
    # 根据num排序，降序输出
    l = sorted(new.items(), key=lambda item: item[1], reverse=True)
    f = open(filename, "w")
    for i in l:
        f.writelines(i[0] + "\t" + str(i[1]) + "\n")
    f.close()
