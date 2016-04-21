# -*- coding:utf-8 -*-
import requests
import re
from apscheduler.schedulers.blocking import BlockingScheduler
from python.alert import *
import os

URL_DES = "http://dev.mysql.com/downloads/connector/python/"
RE_STR = "Python 3.5"
scheduler = BlockingScheduler()


@scheduler.scheduled_job("cron", hour="0/2", day="*")
def task():
    check(RE_STR, URL_DES)


def check(re_str, url):
    rep = requests.get(url)
    text = rep.text
    match = re.compile(re_str)
    if match.findall(text):
        checkMysqlVersionWithPython35_alert()
scheduler.start()
