# Form implementation generated from reading ui file '.\create_user.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(619, 406)
        self.group_box_create_user = QtWidgets.QGroupBox(parent=Form)
        self.group_box_create_user.setGeometry(QtCore.QRect(20, 20, 281, 181))
        self.group_box_create_user.setObjectName("group_box_create_user")
        self.button_create = QtWidgets.QPushButton(parent=self.group_box_create_user)
        self.button_create.setGeometry(QtCore.QRect(20, 130, 241, 24))
        self.button_create.setObjectName("button_create")
        self.line_edit_username = QtWidgets.QLineEdit(parent=self.group_box_create_user)
        self.line_edit_username.setGeometry(QtCore.QRect(100, 40, 161, 22))
        self.line_edit_username.setObjectName("line_edit_username")
        self.line_edit_password = QtWidgets.QLineEdit(parent=self.group_box_create_user)
        self.line_edit_password.setGeometry(QtCore.QRect(100, 80, 161, 22))
        self.line_edit_password.setObjectName("line_edit_password")
        self.label_username = QtWidgets.QLabel(parent=self.group_box_create_user)
        self.label_username.setGeometry(QtCore.QRect(20, 40, 81, 21))
        self.label_username.setObjectName("label_username")
        self.label_password = QtWidgets.QLabel(parent=self.group_box_create_user)
        self.label_password.setGeometry(QtCore.QRect(20, 80, 81, 21))
        self.label_password.setObjectName("label_password")
        self.group_box_change_password = QtWidgets.QGroupBox(parent=Form)
        self.group_box_change_password.setGeometry(QtCore.QRect(320, 20, 281, 181))
        self.group_box_change_password.setObjectName("group_box_change_password")
        self.label_change_username = QtWidgets.QLabel(parent=self.group_box_change_password)
        self.label_change_username.setGeometry(QtCore.QRect(20, 40, 81, 21))
        self.label_change_username.setObjectName("label_change_username")
        self.label_change_password = QtWidgets.QLabel(parent=self.group_box_change_password)
        self.label_change_password.setGeometry(QtCore.QRect(20, 80, 81, 21))
        self.label_change_password.setObjectName("label_change_password")
        self.edit_username_change = QtWidgets.QLineEdit(parent=self.group_box_change_password)
        self.edit_username_change.setGeometry(QtCore.QRect(100, 40, 161, 20))
        self.edit_username_change.setObjectName("edit_username_change")
        self.edit_password_change = QtWidgets.QLineEdit(parent=self.group_box_change_password)
        self.edit_password_change.setGeometry(QtCore.QRect(100, 80, 161, 20))
        self.edit_password_change.setObjectName("edit_password_change")
        self.button_change_password = QtWidgets.QPushButton(parent=self.group_box_change_password)
        self.button_change_password.setGeometry(QtCore.QRect(20, 130, 241, 23))
        self.button_change_password.setObjectName("button_change_password")
        self.group_box_delete_users = QtWidgets.QGroupBox(parent=Form)
        self.group_box_delete_users.setGeometry(QtCore.QRect(20, 210, 281, 181))
        self.group_box_delete_users.setObjectName("group_box_delete_users")
        self.label_delete_user = QtWidgets.QLabel(parent=self.group_box_delete_users)
        self.label_delete_user.setGeometry(QtCore.QRect(20, 40, 81, 21))
        self.label_delete_user.setObjectName("label_delete_user")
        self.edit_delete_user = QtWidgets.QLineEdit(parent=self.group_box_delete_users)
        self.edit_delete_user.setGeometry(QtCore.QRect(110, 40, 151, 21))
        self.edit_delete_user.setObjectName("edit_delete_user")
        self.button_delete_user = QtWidgets.QPushButton(parent=self.group_box_delete_users)
        self.button_delete_user.setGeometry(QtCore.QRect(20, 70, 241, 23))
        self.button_delete_user.setObjectName("button_delete_user")
        self.group_box_created_users = QtWidgets.QGroupBox(parent=Form)
        self.group_box_created_users.setGeometry(QtCore.QRect(320, 210, 281, 181))
        self.group_box_created_users.setObjectName("group_box_created_users")
        self.table_created_users = QtWidgets.QTableView(parent=self.group_box_created_users)
        self.table_created_users.setGeometry(QtCore.QRect(20, 50, 241, 111))
        self.table_created_users.setObjectName("table_created_users")
        self.button_show_users = QtWidgets.QPushButton(parent=self.group_box_created_users)
        self.button_show_users.setGeometry(QtCore.QRect(20, 20, 241, 23))
        self.button_show_users.setObjectName("button_show_users")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.group_box_create_user.setTitle(_translate("Form", "Create new user"))
        self.button_create.setText(_translate("Form", "Create new user"))
        self.label_username.setText(_translate("Form", "Username"))
        self.label_password.setText(_translate("Form", "Password"))
        self.group_box_change_password.setTitle(_translate("Form", "Change password"))
        self.label_change_username.setText(_translate("Form", "Username"))
        self.label_change_password.setText(_translate("Form", "New Password"))
        self.button_change_password.setText(_translate("Form", "Change password"))
        self.group_box_delete_users.setTitle(_translate("Form", "Delete users"))
        self.label_delete_user.setText(_translate("Form", "Username"))
        self.button_delete_user.setText(_translate("Form", "Delete user"))
        self.group_box_created_users.setTitle(_translate("Form", "Created users"))
        self.button_show_users.setText(_translate("Form", "Show users"))
