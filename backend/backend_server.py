# -*- coding: utf-8 -*-
from flask import Flask,request
from flask_restful import Resource,Api
from flask_sqlalchemy import SQLAlchemy
import json

app=Flask(__name__)
# 配置数据库的详细信息
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://cekai_17:123456@192.168.224.140/test_backend_17'
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

# 定义测试用例接口
# class TestCaseServer(Resource):
#     # get方法代表接收get请求
#     def get(self):
#         """
#         获取所有测试用例数据
#         :return:
#         """
#         option=request.args.get("option")
#         if option=="get_testcase":
#             # 查找所有的测试用例
#             test_cases=TestCase.query.all()
#             # 对所有的测试用例进行格式化
#             format_test_cases=[i.as_dict() for i in test_cases]
#             return format_test_cases
#         # 如果url中存在option参数为del_testcase代表要删除用例
#         elif option=="del_testcases":
#             # 利用nodeids参数指明要删除的用例
#             # ****删除多个的时候的url格式http://127.0.0.1:5000/testcase?option=del_testcases&nodeids=nodeid_0,nodeid_1*********代码中用nodeids.split(",")
#             nodeids=request.args.get("nodeids")
#             print(nodeids.split(","))
#             for nodeid in nodeids.split(","):
#                 # 查询此用例后，进行删除
#                 testcase=TestCase.query.filter_by(nodeid=nodeid).first()
#                 db.session.delete(testcase)
#             db.session.commit()
#             return {"msg":"delete success"}

# 定义测试用例接口
class TestCaseAdd(Resource):
    def post(self):
        """
        新增用例
        :return:
        """
        data=TestCase(**request.json)
        db.session.add(data)
        db.session.commit()
        return {"msg":"OK"}

class TestCaseDelete(Resource):
    def get(self):
        nodeids = request.args.get("nodeids")
        print(nodeids.split(","))
        for nodeid in nodeids.split(","):
            # 查询此用例后，进行删除
            testcase = TestCase.query.filter_by(nodeid=nodeid).first()
            db.session.delete(testcase)
        db.session.commit()
        return {"msg": "delete success"}

class TestCaseGet(Resource):
    def get(self):
        #查找所有测试用例
        test_cases=test_cases=TestCase.query.all()
        # 对所有的测试用例进行格式化
        format_test_cases=[i.as_dict() for i in test_cases]
        return format_test_cases


# 定义测试用例接口
class TestCaseUpdate(Resource):
    def post(self):
        """
        更新测试用例
        :return:
        """
        request.body=request.json
        testcase=TestCase.query.filter_by(nodeid=request.body.get("nodeid")).first()
        testcase.description=request.body.get("description")
        db.session.commit()
        return {'msg':"update success"}

#添加路由
# r=requests.post("http://127.0.0.1:5000/testcase/add",json={"nodeid":"nodeid_99","description":"add case 99"})
api.add_resource(TestCaseAdd,'/testcase/add')

# http://127.0.0.1:5000/testcase/delete?nodeids=nodeid_3
api.add_resource(TestCaseDelete,'/testcase/delete')

# http://127.0.0.1:5000/testcase/get
api.add_resource(TestCaseGet,'/testcase/get')

# r=requests.post("http://127.0.0.1:5000/testcase/update",json={"nodeid":"nodeid_3","description":"aaaaaaaaaaaa"})
api.add_resource(TestCaseUpdate,'/testcase/update')

if __name__=='__main__':
    # db.drop_all()
    # db.create_all()
    # for i in range(5):
    #     data=TestCase(nodeid='nodeid_'+str(i))
    #     db.session.add(data)
    # db.session.commit()

    app.run(debug=True)




