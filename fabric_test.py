#!/usr/bin/env python
#-*- coding: utf-8 -*-

from fabric.api import *

env.user = 'jeff'
env.hosts = ['10.0.0.26','10.0.0.27']
env.password = 'redhat'

def print_hostname():
    with settings(warn_only=True):
        run("hostname")

def print_ip():
    with settings(warn_only=True):
        run("ip addr show | grep '10'")

def deploy():
    execute(print_hostname)
    execute(print_ip)