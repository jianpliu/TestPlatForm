# -*- coding: utf-8 -*-
from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy



app=Flask(__name__)
# 配置数据库的详细信息
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://cekai_17:123456@192.168.224.142/test_backend_17'

# 将flask实例加载到flask-restful中
# api=Api(app)


app.config["SECRETY_KEY"]="SDE17CK"

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



api=Api(app)
db=SQLAlchemy(app)

# 使用CORS解决同源问题
CORS(app)

def router():
    from backend.api.login import Login

    api.add_resource(Login, '/login')

    from backend.api.testcase import TestCaseAdd
    api.add_resource(TestCaseAdd, '/testcase/add')

    # http://127.0.0.1:5000/testcase/delete?nodeids=nodeid_3
    from backend.api.testcase import TestCaseDelete
    api.add_resource(TestCaseDelete, '/testcase/delete')

    # http://127.0.0.1:5000/testcase/get
    from backend.api.testcase import TestCaseGet
    api.add_resource(TestCaseGet, '/testcase/get')

    # r=requests.post("http://127.0.0.1:5000/testcase/update",json={"nodeid":"nodeid_3","description":"aaaaaaaaaaaa"})
    from backend.api.testcase import TestCaseUpdate
    api.add_resource(TestCaseUpdate, '/testcase/update')




if __name__=='__main__':
    # db.drop_all()
    # db.create_all()
    # for i in range(5):
    #     data=TestCase(nodeid='nodeid_'+str(i))
    #     db.session.add(data)
    # db.session.commit()
    router()
    app.run(debug=True)




