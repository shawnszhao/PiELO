# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created: Wed Apr 06 12:16:24 2016
#      by: PyQt4 UI code generator 4.10.4
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.Title = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setObjectName(_fromUtf8("Title"))
        self.gridLayout.addWidget(self.Title, 0, 0, 1, 5, QtCore.Qt.AlignHCenter)
        self.ChangePassword = QtGui.QPushButton(self.centralwidget)
        self.ChangePassword.setObjectName(_fromUtf8("ChangePassword"))
        self.gridLayout.addWidget(self.ChangePassword, 2, 1, 1, 1)
        self.EnterScore = QtGui.QPushButton(self.centralwidget)
        self.EnterScore.setObjectName(_fromUtf8("EnterScore"))
        self.gridLayout.addWidget(self.EnterScore, 2, 2, 1, 1)
        self.CreateNewPlayer = QtGui.QPushButton(self.centralwidget)
        self.CreateNewPlayer.setObjectName(_fromUtf8("CreateNewPlayer"))
        self.gridLayout.addWidget(self.CreateNewPlayer, 2, 0, 1, 1)
        self.LoadPlayerGraph = QtGui.QPushButton(self.centralwidget)
        self.LoadPlayerGraph.setObjectName(_fromUtf8("LoadPlayerGraph"))
        self.gridLayout.addWidget(self.LoadPlayerGraph, 2, 3, 1, 1)
        self.LoadPlayerInfo = QtGui.QPushButton(self.centralwidget)
        self.LoadPlayerInfo.setObjectName(_fromUtf8("LoadPlayerInfo"))
        self.gridLayout.addWidget(self.LoadPlayerInfo, 2, 4, 1, 1)
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setMinimumSize(QtCore.QSize(782, 0))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.Title.setText(_translate("MainWindow", "Sammy\'s BP Leaderboard", None))
        self.ChangePassword.setText(_translate("MainWindow", "Change Password", None))
        self.EnterScore.setText(_translate("MainWindow", "Enter Score", None))
        self.CreateNewPlayer.setText(_translate("MainWindow", "Create New Player", None))
        self.LoadPlayerGraph.setText(_translate("MainWindow", "Load Player Graphs", None))
        self.LoadPlayerInfo.setText(_translate("MainWindow", "Load Player Info", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Player", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ELO", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Sinks Per Game", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "New Column", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Points per Sink", None))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "New Column", None))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Favorite Opp", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

