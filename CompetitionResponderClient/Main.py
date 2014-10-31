# -*- coding: utf-8 -*-
'''
Created on 2014年9月16日

@author: Ying
'''

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4 import Qt
from MainWindow_ui import Ui_MainWindow
import requests
import socket


class MyMainWindow(Ui_MainWindow):

    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__()
        # QtGui.QMainWindow.__init__(self,parent)
        self.ui = Ui_MainWindow(self)
        self.ui.setupUi(self)
        self.setupConnect()

    def setupConnect(self):
        self.ui.pushButton.clicked.connect(self.answer)
        self.ui.pushButton_bind.clicked.connect(self.bind)

    def answer(self):
        self.s.sendto('answer'.encode(), self.desc)

    def bind(self):
        self.desc = ('<broadcast>', 12345)
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        bindstr = 'name' + self.ui.lineEdit_Name.text()
        self.s.sendto(bindstr.encode(), self.desc)

app = QtGui.QApplication(sys.argv)
widget = MyMainWindow()
widget.show()
sys.exit(app.exec_())
