# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\GitHub\CompetitionResponderServer\MainWindow.ui'
#
# Created: Fri Oct 31 14:51:09 2014
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(QtGui.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(666, 580)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label_title = QtGui.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(90, 10, 491, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setPointSize(20)
        self.label_title.setFont(font)
        self.label_title.setTextFormat(QtCore.Qt.AutoText)
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setMargin(0)
        self.label_title.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_title.setObjectName(_fromUtf8("label_title"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 380, 351, 141))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setPointSize(40)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_bind = QtGui.QPushButton(self.centralwidget)
        self.pushButton_bind.setGeometry(QtCore.QRect(150, 320, 351, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setPointSize(20)
        self.pushButton_bind.setFont(font)
        self.pushButton_bind.setObjectName(_fromUtf8("pushButton_bind"))
        self.label_1 = QtGui.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(70, 80, 131, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑 Light"))
        font.setPointSize(12)
        self.label_1.setFont(font)
        self.label_1.setTextFormat(QtCore.Qt.AutoText)
        self.label_1.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_1.setMargin(0)
        self.label_1.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_1.setObjectName(_fromUtf8("label_1"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 110, 131, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑 Light"))
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_2.setMargin(0)
        self.label_2.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 140, 131, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑 Light"))
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_3.setMargin(0)
        self.label_3.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 170, 131, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑 Light"))
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_4.setMargin(0)
        self.label_4.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(70, 200, 131, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑 Light"))
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setTextFormat(QtCore.Qt.AutoText)
        self.label_5.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_5.setMargin(0)
        self.label_5.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(70, 230, 131, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑 Light"))
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setTextFormat(QtCore.Qt.AutoText)
        self.label_6.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_6.setMargin(0)
        self.label_6.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(70, 260, 131, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑 Light"))
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setTextFormat(QtCore.Qt.AutoText)
        self.label_7.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_7.setMargin(0)
        self.label_7.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_team_got = QtGui.QLabel(self.centralwidget)
        self.label_team_got.setGeometry(QtCore.QRect(260, 150, 341, 131))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑 Light"))
        font.setPointSize(30)
        self.label_team_got.setFont(font)
        self.label_team_got.setTextFormat(QtCore.Qt.AutoText)
        self.label_team_got.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_team_got.setMargin(0)
        self.label_team_got.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_team_got.setObjectName(_fromUtf8("label_team_got"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(620, 520, 41, 16))
        self.label.setObjectName(_fromUtf8("label"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 666, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_title.setText(_translate("MainWindow", "<html><head/><body><p>清华创客空间 万圣节游戏夜！</p></body></html>", None))
        self.pushButton.setText(_translate("MainWindow", "开始抢答！！", None))
        self.pushButton_bind.setText(_translate("MainWindow", "开始绑定", None))
        self.label_1.setText(_translate("MainWindow", "<html><head/><body><p>第一队</p></body></html>", None))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p>第二队</p></body></html>", None))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p>第三队</p></body></html>", None))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p>第四队</p></body></html>", None))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p>第五队</p></body></html>", None))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p>第六队</p></body></html>", None))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p>第七队</p></body></html>", None))
        self.label_team_got.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>", None))
        self.label.setText(_translate("MainWindow", "By 毕滢", None))
