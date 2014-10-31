# -*- coding: utf-8 -*-
'''
Created on 2014年9月16日

@author: Ying
'''

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4 import Qt
from PyQt4.QtCore import pyqtSignal
from MainWindow_ui import Ui_MainWindow
import socket
import threading
import traceback

team_ip_record = dict()
team_name_record = dict()
team_name_list = []


class BindThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.thread_stop = False
        self.myCommunicator = MyCommunicator()
        self.host = ''
        self.port = 12345
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.s.bind((self.host, self.port))
        self.team_count = 0

    def run(self):
        while not self.thread_stop:
            try:
                msg, addr = self.s.recvfrom(8192)
                print("Receive data from:", addr)
                print("\n", msg.decode())
                msgstr = msg.decode()
                print(msgstr)
                if msgstr[0:4] == 'name':
                    team_name = msgstr[4:len(msgstr)]
                    print(team_name)
                    if not team_ip_record.get(str(addr[0])):
                        print('in')
                        team_ip_record[str(addr[0])] = team_name
                        team_name_record[team_name] = self.team_count
                        team_name_list.append(team_name)
                        self.team_count = self.team_count + 1
                        self.myCommunicator.sendSignal()
            except:
                    traceback.print_exc()

    def stop(self):
        self.thread_stop = True
        self.s.close()


class MyCommunicator(QtCore.QObject):

    trigger = pyqtSignal(name='DataReceived')

    def __init__(self, parent=None):
        super(MyCommunicator, self).__init__()

    def sendSignal(self):
        self.trigger.emit()


class MyMainWindow(Ui_MainWindow):

    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__()
        # QtGui.QMainWindow.__init__(self,parent)
        self.ui = Ui_MainWindow(self)
        self.ui.setupUi(self)
        self.setupConnect()
        self.start_bind = False
        self.start_answer = False

    def setupConnect(self):
        self.ui.pushButton.clicked.connect(self.answer)
        self.ui.pushButton_bind.clicked.connect(self.bind)

    def answer(self):
        if not self.start_answer:
            self.ui.pushButton.setText('清除')
            self.host = ''
            self.port = 12345
            self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            self.s.bind((self.host, self.port))
            while True:
                try:
                    msg, addr = self.s.recvfrom(8)
                    print("Receive data from:", addr)
                    team_name = team_ip_record[str(addr[0])]
                    print('1')
                    print(team_name)
                    self.ui.label_team_got.setText(team_name)
                    print('2')
                    self.start_answer = True
                    print('Done')
                    break
                except:
                    pass
            self.s.close()
        else:
            self.ui.pushButton.setText('开始抢答！！')
            self.ui.label_team_got.setText('')
            self.start_answer = False

    def bind(self):
        if not self.start_bind:
            print('start bind')
            self.start_bind = True
            self.ui.pushButton_bind.setText('停止绑定')
            self.myBindThread = BindThread()
            self.myBindThread.myCommunicator.trigger.connect(self.updateName)
            self.myBindThread.start()
        else:
            self.start_bind = False
            self.ui.pushButton_bind.setText('开始绑定')
            self.myBindThread.stop()

    def updateName(self):
        try:
            self.ui.label_1.setText(team_name_list[0])
            self.ui.label_2.setText(team_name_list[1])
            self.ui.label_3.setText(team_name_list[2])
            self.ui.label_4.setText(team_name_list[3])
            self.ui.label_5.setText(team_name_list[4])
            self.ui.label_6.setText(team_name_list[5])
            self.ui.label_7.setText(team_name_list[6])
        except:
            pass

app = QtGui.QApplication(sys.argv)
widget = MyMainWindow()
widget.show()
sys.exit(app.exec_())
