# -*- coding:utf-8 -*-
import requests
import re
from apscheduler.schedulers.blocking import BlockingScheduler
import os

CURRENT_DIR = os.getcwd()
INFO_FILE_DIR = CURRENT_DIR.replace("python", "vbs")
INFO_FILE_SCRIPT = INFO_FILE_DIR + "\\mysqlVersionPython35.vbs"
URL_DES = "http://dev.mysql.com/downloads/connector/python/"
RE_STR = "Python 3.5"
scheduler = BlockingScheduler()


@scheduler.scheduled_job("cron", hour="0/2", day="*")
def task():
    check(RE_STR, URL_DES, INFO_FILE_SCRIPT)


def check(re_str, url, info):
    rep = requests.get(url)
    text = rep.text
    match = re.compile(re_str)
    if match.findall(text):
        os.system(info)
scheduler.start()
