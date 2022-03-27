# -*- coding: utf-8 -*-

#获取Jenkins的版本
from jenkinsapi.jenkins import Jenkins
#Jenkins服务
BASE_URL="http://192.168.224.137:8083/"
#Jenkins服务对应的用户名
USERNAME="Nancy"
#Jenkins服务对应的token
PASSWORD="115d5043058dc5962e7de7e7939b25391a"
jenkins_hogwarts=Jenkins(BASE_URL,USERNAME,PASSWORD)
print(jenkins_hogwarts.version)

#获取jenkin的job对象
job=jenkins_hogwarts.get_job("11")
#构建hogwarts_job
# job.invoke()
#构建的"11"job,传入的值必须是字典，key对应jenkins设置的参数名
job.invoke(build_params={"task":"hogwarts_Ad"})
#获取job最后一次构建的编号
print(job.get_last_buildnumber())