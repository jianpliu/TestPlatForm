# -*- coding: utf-8 -*-
import requests


class TestTestCase:
    def test_get_right_testccase(self):
        r=requests.get("http://localhost:5000/login",auth=("xxx","xx"))
        # token=r.json().get("access_token")
        token = r.json()["access_token"]
        r=requests.get("http://127.0.0.1:5000/testcase/get",auth=(token,""))
        assert r.status_code==200
        # assert r.json().get("msg")=="OK"
        assert r.json()["msg"] == "OK"

    def test_get_error_testccase(self):
        r=requests.get("http://localhost:5000/login",auth=("xxx","xx"))
        # token=r.json().get("access_token")
        token = ""
        r=requests.get("http://127.0.0.1:5000/testcase/get",auth=(token,""))
        assert r.status_code==401
