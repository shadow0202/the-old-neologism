import subprocess

import time

from utils2 import mysqlhelp

mh = mysqlhelp.MysqlHelp()

t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
sql = "INSERT INTO show_newwords_runtime(time) VALUES('%s')" % (t)
mh.insert(sql=sql)