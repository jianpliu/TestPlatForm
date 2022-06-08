# -*- coding: utf-8 -*-
from flask import g
from flask_httpauth import HTTPBasicAuth



auth = HTTPBasicAuth()


"""
auth的username在登录时，是用户名，但是在登陆后（第二次登录第三次登录，是token）,有2个功能，既能校验用户名是否合法，又能检验token是否合法
无论是登陆接口还是获取用例接口，都是回调的这一个方法
"""
# 编写回调函数，当进行登录时，会回调此函数
@auth.verify_password
def verify_password(username, password):
    # 初始化auth
    from backend.data_base.user_table import User
    print(username)
    print(password)
    # 进行token校验



    user=User.check_token(username)
    # 如果检验结果错误，或者超时，就认为此时是登陆接口
    # 如果检验成功，就认为此时是其他接口（获取用例）
    if not user:
        user=User.query.filter_by(username=username).first()
        if not user or user.password!=password:
            return False
    # 如果token符合要求，或者用户名，密码正确
    # flask的g代表flask的本地线程变量->flask线程可共享使用
    g.user=user
    return True