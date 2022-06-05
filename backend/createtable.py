# -*- coding: utf-8 -*-
from flask import Flask,request
from flask_restful import Resource,Api
from flask_sqlalchemy import SQLAlchemy
import json

app=Flask(__name__)
# 配置数据库的详细信息
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://cekai_17:123456@192.168.224.142/test_backend_17'
# 初始化一个db
db=SQLAlchemy(app)
# 将flask实例加载到flask-restful中
api=Api(app)


class TestCase(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    nodeid=db.Column(db.String(80),unique=True,nullable=False)
    description=db.Column(db.String(120),unique=False,nullable=True)


    def as_dict(self):
        """
        返回测试用例的数据
        :return:
        """
        return {"id":self.id,"nodeid":self.nodeid,"description":self.description}


if __name__=='__main__':
    db.drop_all()
    db.create_all()



    # 运行后会生成test_case1表格