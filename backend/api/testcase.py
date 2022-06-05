# -*- coding: utf-8 -*-


# 定义测试用例接口
from flask import request
from flask_restful import Resource

# from backend.backend_server import db
from backend.api.verify_token import auth
from backend.backend_server import db, api
from backend.data_base.testcase_table import TestCase


class TestCaseAdd(Resource):
    # method_decorators = {'get': [auth.login_required]} 这里可以不什么类型，就是对所有的类get、post、delete都有装饰器效果
    method_decorators = [auth.login_required]
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
    method_decorators = [auth.login_required]
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
    method_decorators = [auth.login_required]
    def get(self):
        #查找所有测试用例
        # test_cases=test_cases=TestCase.query.all()
        test_cases = TestCase.query.all()
        # 对所有的测试用例进行格式化
        format_test_cases=[i.as_dict() for i in test_cases]
        return {"msg":"OK","data": format_test_cases}


# 定义测试用例接口
class TestCaseUpdate(Resource):
    method_decorators = [auth.login_required]
    def post(self):
        """
        更新测试用例
        :return:
        """
        request.body=request.json
        testcase=TestCase.query.filter_by(nodeid=request.body.get("nodeid")).first()
        testcase.description=request.body.get("description")
        db.session.commit()
        return {'msg':"update su ccess"}

