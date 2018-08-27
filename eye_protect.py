# -*- coding:utf-8 -*-
from apscheduler.schedulers.blocking import BlockingScheduler

from alert import alert

scheduler = BlockingScheduler()


@scheduler.scheduled_job("cron", minute="*/40", hour="*")
def eye_protect():
    alert("友情提示", "40分钟了，起来溜达溜达吧！")

scheduler.start()
