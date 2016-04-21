# coding=utf-8
###########################################
# File: timer.py
# Desc: 定时器
# Author: zhangyufeng
# History: 2015/01/01 zhangyufeng 新建
###########################################
import threading
import time


class Timer:
    u'''
            此类是一个定时器.
            其中i作为计数变量，
            timeSpace为时间间隔(默认为None，实例化后需要手动设定)，
            timeOut为超时周期(默认为None，非必填项，根据实际情况实例化后设定)
    '''
    i = -1
    timeSpace = None
    timeOut = None

    def run(self):
        global i
        global timeSpace
        global timeOut
        self.i = self.i + 1
        timeNow = time.strftime(
            '%Y-%m-%d  %H:%M:%S', time.localtime(time.time()))
        print("Run!  ", timeNow)
        if self.timeOut is not None:
            if self.i != self.timeOut:
                self.tmp = threading.Timer(self.timeSpace, self.run)
                self.tmp.start()
        else:
            self.tmp = threading.Timer(self.timeSpace, self.run)
            self.tmp.start()
