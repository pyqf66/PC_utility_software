# -*- coding:utf-8 -*-
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMessageBox
import sys


def eye_protect_alert():
    app=QApplication(sys.argv)
    msg_box=QMessageBox(QMessageBox.warning,"友情提示","40分钟了，起来溜达溜达吧！")
    msg_box.show()
    app.exec()

def checkMysqlVersionWithPython35_alert():
    app=QApplication(sys.argv)
    msg_box=QMessageBox(QMessageBox.warning,"友情提示","mysql的python3.5驱动出来了！")
    msg_box.show()
    app.exec()
