# -*- coding:utf-8 -*-
import re

import requests
from apscheduler.schedulers.blocking import BlockingScheduler

from alert import alert

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
        alert("情友提示", "mysql的python3.5驱动出来了！")

scheduler.start()
