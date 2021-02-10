import pymysql
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

###连接数据库
conn=pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='mj0526yy',
    db='bigdata'
    )
###创建游标,使用cursor()方法获取数据库的操作游标
cur=conn.cursor()
###执行操作
cur.execute("SELECT `PMM_DATETIME`,`ECELL_NAME`,`pmS1SigConnEstabAtt`,`pmS1SigConnEstabSucc` FROM `magaga` WHERE `ECELL_NAME`='ABEVFM2'")
data=cur.fetchall()#元组里面嵌套元组,此时数据每一行为一个元组。
data=pd.DataFrame(data,columns=['PMM_DATETIME','ECELL_NAME','pmS1SigConnEstabAtt','pmS1SigConnEstabSucc'])
data=data.set_index(['PMM_DATETIME'])#将时间序列作为索引，新学知识
