# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
# 配置数据库的详细信息
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://cekai_17:123456@192.168.224.139/test_backend_17'
# 初始化一个db
db=SQLAlchemy(app)

# 使用db,可以让User类 映射到数据库中的User表
class User(db.Model):
    # 以下字段代表数据库中的表
    # db.Integer是整型，primary_key代表主键，唯一标识一条数据，是一条数据的身份证
    id=db.Column(db.Integer,primary_key=True)
    # db.String(80) 代表80个字符的字符串
    #unique代表是不是唯一
    #nullable是否可为空，如果为False,说明为必填项
    username=db.Column(db.String(88),unique=True,nullable=False)
    # email=db.Column(db.String(120),unique=True,nullable=False)
    # email2=db.Column(db.String(120),unique=True,nullable=False)
    description=db.Column(db.String(120),unique=False,nullable=True)

    def __repr__(self):
        # return '<User %r>' % self.username
        return f'<User {self.username} {self.description}>'


class Task(db.Model):
    task_id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(88),unique=True,nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


if __name__=="__main__":

    # # 删除（要想往已有的数据库中添加一个字段，先drop删除掉表，再重新新建）
    # db.drop_all()
    # # 在远程数据库中创建表
    # db.create_all()
    # # ————————————————————————————————————————————————————

    # # 向数据库中添加一条数据
    # #实例化User类\
    # for i in range(1,20):
    #     data=User(username="wangwu"+str(i),description="i'm wangwu")
    #     # 把类添加到sqlalchemy中
    #     db.session.add(data)
    # # 把操作提交
    # db.session.commit()
    # # # --------------------------------------------------------------------------------------------------------

    #查询
    # 在User表中查数据，就使用User.query     filter_by(id=1,name='aa')
    # first指：获取第一个结果
    # result=User.query.filter_by(id=1).all()
    result = User.query.all()
    result=[i for i in result if "0" in i.username]
    print(result)

    # # -------------------------------------------------更新-----------------------------------------------------
    # # 先过滤出想要修改的数据，然后对数据进行修改，修改完成后可以使用db.session.commit()进行提交
    # user=User.query.filter_by(username='wangwu1').first()
    # print(type(user))
    # print(user)
    # user.description="hello!"
    # db.session.commit()

    #  -------------------------------------------------删除-----------------------------------------------------
    user=User.query.filter_by(username='wangwu1').first()
    db.session.delete(user)
    db.session.commit()
