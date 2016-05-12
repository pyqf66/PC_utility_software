# -*- coding:utf-8 -*-
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMessageBox
import sys


def alert(remind, message):
    app = QApplication(sys.argv)
    msg_box = QMessageBox(QMessageBox.Warning, remind, message)
    msg_box.show()
    app.exec_()
