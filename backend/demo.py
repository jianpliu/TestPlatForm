# -*- coding: utf-8 -*-
from flask import Flask
from flask import request

# 初始化Flask实例
#Flask是一个wsgi应用，（WSGI 是一套协议，是web应用与服务器交互更通顺）
#__name__给Flask 一个名称
app=Flask(__name__)

#定义了路由，当访问路由中定义的url时，就会执行下面的函数
#/代表根，也就是说，当浏览器什么都不输入的时候，就访问了根
@app.route("/")
def hello_word():
    #Flask 函数的返回值，默认是html类型
    #如果返回是字典，就是json类型
    return "<p>Hello World!1<p>"


#methods可以指定监听的类型，可以是post get put...
@app.route('/abc/<int:tmp>',methods=['get','post'])
def hello(tmp):
    print(request.data)
    print(request.json)
    print(tmp)
    return "hello"




#可以通过http://127.0.0.1:5000/param?a=b&c=k 来发送两个参数a=b和c=k,返回
# {
#   "a": "b",
#   "c": "k"
# }
@app.route("/param",methods=["GET","POST"])
def get_param():
    # return "<p>Fine thank you!</p>"
    # 可以利用request.args提取两个参数
    return request.args


@app.route("/param1",methods=["POST"])
def get_param1():
    # return "<p>Fine thank you!</p>"
    # 可以利用request.json获取post传过来的请求体
    return request.json

#Flask中<abc>代表变量，会把真实url的<abc>中的内容传递给对应变量
@app.route("/param/<abc>")
def get_var(abc):
    return abc

if __name__=='__main__':
    #运行服务,Flask默认会监听127.0.0.1:5000，只要发送get（或者其他）请求，就能触发路由
    #debug参数：启动调试模式（当代码发生变化时，Flask会自动刷新，使改动生效）
    app.run(debug=True,host="0.0.0.0")
