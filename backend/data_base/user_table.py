# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# 用于生成具有时间维护的token
from itsdangerous import TimedJSONWebSignatureSerializer, BadSignature, SignatureExpired
import datetime


# app=Flask(__name__)
# # 配置数据库的详细信息
# app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://cekai_17:123456@192.168.224.142/test_backend_17'
# # 配置token种子
from backend.backend_server import app, db


# app.config["SECRETY_KEY"]="SDE17CK"
# # 初始化一个db
# db=SQLAlchemy(app)

# 使用db,可以让User类 映射到数据库中的User表



class User(db.Model):
    """
    用户表，需要有账号、密码、邮箱
    """
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(88),unique=True,nullable=False)
    password = db.Column(db.String(88), unique=True, nullable=False)
    email=db.Column(db.String(120),unique=False,nullable=False)
    # 创建日期

    def __repr__(self):
        # return '<User %r>' % self.username
        return f'<User {self.username}>'

    def generate_token(self,expires_in=3*3600):
        """
        生成token
        :return:
        """
        # 第一个参数secret_key是随机数种子     app.config["SECRETY_KEY"]：token种子 用于生成token 其值可以是随机的
        # expire_in代表超时时间
        serializer=TimedJSONWebSignatureSerializer(app.config["SECRETY_KEY"],expires_in)
        token_id=self.username+self.password+str(datetime.datetime.now())
        # dumps用于反序列化（把Python对象转成字符串），生成token
        token=serializer.dumps({"id":self.id,"token_id":token_id}).decode()
        # 需要decode是因为dump产生的是字节，需要进行decode解码成字符串
        return token



    # 类方法 方便外界调用，同时此方法不会用到对象中的数据
    @classmethod
    def check_token(cls,token):
        """
        校验token
        :return:User or None
        """
        serializer = TimedJSONWebSignatureSerializer(app.config["SECRETY_KEY"])
        try:
            # loads用于序列化，把Token转换成Python对象
            token_loads_result=serializer.loads(token)
        #     如果Token 校验失败，会抛出BadSignature
        #     如果Token 校验超时，会抛出SignatureExpired
        except (BadSignature,SignatureExpired):
            return None
        # User.query.get表示利用id找到User表中的一个字段,返回user对象（因为用了ORM：将数据库字段映射到python对象上）
        return User.query.get(token_loads_result["id"])






# class Task(db.Model):
#     task_id=db.Column(db.Integer,primary_key=True)
#     name=db.Column(db.String(88),unique=True,nullable=False)
#
#     def __repr__(self):
#         return '<User %r>' % self.username


if __name__=="__main__":
    # 删库
    db.drop_all()
    # 在远程数据库中创建表
    db.create_all()