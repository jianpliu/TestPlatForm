# -*- coding: utf-8 -*-
import requests


class TestLogin:
    BASE_URL="http://localhost:5000"


    def test_login(self):
        # 其中auth表示要输入的注册信息，比如账号和密码
        r=requests.get(self.BASE_URL+"/login",auth=("xxx","xx"))
        assert "access_token" in r.json()

        # 其中auth表示要输入的注册信息，比如账号和密码
        r = requests.get(self.BASE_URL + "/login", auth=("xxx", "abcdef"))
        assert r.status_code==401
