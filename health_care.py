from apscheduler.schedulers.blocking import BlockingScheduler
from lib.alert import *


scheduler = BlockingScheduler()


@scheduler.scheduled_job("cron", day_of_week="thu", hour="14", minute="25", second="00")
def hello():
    alert("友情提示！", "报名时间到了！")
scheduler.start()
