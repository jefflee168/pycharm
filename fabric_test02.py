#!/usr/bin/env python
#-*- coding: utf-8 -*-

from fabric.api import *

# 主机的用户
env.user = 'jeff'

# 定义多台主机
env.roledefs = {
    'db': ['10.0.0.26'],
    'web': ['10.0.0.27'],
}

# 主机密码
env.password = 'redhat'

# 指定服务器执行的命令
@roles('db')
def print_hostname():
    with settings(warns_only=True):
        run('hostname')

# 指定服务器执行的命令
@roles('web')
def print_ip():
    with settings(warns_only=True):
        run("ip addr show|grep '10'")

# 执行多个任务
def deploy():
    execute(print_hostname)
    execute(print_ip)