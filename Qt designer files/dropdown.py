# Form implementation generated from reading ui file '.\mian_window.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 141, 61))
        self.frame.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.CustomContextMenu)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame.setObjectName("frame")
        self.label_active_user = QtWidgets.QLabel(parent=self.frame)
        self.label_active_user.setGeometry(QtCore.QRect(10, 10, 61, 41))
        self.label_active_user.setObjectName("label_active_user")
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setGeometry(QtCore.QRect(80, 10, 47, 41))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menu_bar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menu_bar.setObjectName("menu_bar")
        MainWindow.setMenuBar(self.menu_bar)
        self.status_bar = QtWidgets.QStatusBar(parent=MainWindow)
        self.status_bar.setObjectName("status_bar")
        MainWindow.setStatusBar(self.status_bar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_active_user.setText(_translate("MainWindow", "Active user:"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
