# -*- coding:utf-8 -*-
import os
from apscheduler.schedulers.blocking import BlockingScheduler


CURRENT_DIR = os.getcwd()
EYE_PROTECT_FILE_DIR = CURRENT_DIR.replace("python", "vbs")
EYE_PROTECT_FILE_SCRIPT = EYE_PROTECT_FILE_DIR + "\\eye_protect.vbs"
scheduler = BlockingScheduler()


@scheduler.scheduled_job("cron", minute="40/40", hour="*")
def eye_protect():
    os.system(EYE_PROTECT_FILE_SCRIPT)
scheduler.start()
