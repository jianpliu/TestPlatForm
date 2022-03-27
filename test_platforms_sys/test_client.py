# -*- coding: utf-8 -*-
import pymysql

db=pymysql.connect(
    host='stuq.ceshiren.com',
    user='hogwarts_python',
    passwd='hogwarts_python',
    db='hogwarts_python',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor  #词典游标：将查询结果显示成dict
)

def test_conn():
    with db.cursor() as cursor:
        sql="show tables;"
        cursor.execute(sql)
        print(sql)
        print(cursor.fetchall())

def test_select():
    with db.cursor() as c:
        sql="select * from sevenituby_user where username=%s"
        c.execute(sql,["demo"]) #是向sql里边传参username="demo"
        print(c.fetchall())

        #default
        #((11,'demo','demo_password','demo@ceshiren.com'))

        #cursorclass=pymysql.cursors.DictCursor  #词典游标：将查询结果显示成dict
        # [{'id':11, 'username':'demo','password':'demo_password', 'email':'demo@ceshiren.com'}]


