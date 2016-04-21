# -*- coding:utf-8 -*-
from apscheduler.schedulers.blocking import BlockingScheduler
from python.alert import *


scheduler = BlockingScheduler()


@scheduler.scheduled_job("cron", minute="40/40", hour="*")
def eye_protect():
    eye_protect_alert()
scheduler.start()
