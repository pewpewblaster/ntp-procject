from PyQt6 import QtCore, QtGui, QtWidgets
from access_connector import check_credentials
from main_form import Ui_MainWindow
from create_user_form import Ui_Form
from winreg_utils import win_reg_app_data
from SQLite.sqlite3dll_handler_class import JwtDatabaseManager

''' global variable'''

only_once = True
supported_languages = ["French",
                       "Croatian",
                       "English",
                       "German",
                       "Spanish"]

''' classes '''
class login_form(object):
    def login_ui(self, Form):
        self.Form = Form
        Form.setObjectName("Form")
        
        ############
        # test #####
        ############
        object_test = JwtDatabaseManager()
        
        # login button
        self.login_button = QtWidgets.QPushButton(parent=Form)
        self.login_button.setGeometry(QtCore.QRect(20, 160, 91, 21))
        self.login_button.setObjectName("login_button")
        self.login_button.clicked.connect(self.login)

        # exit button
        self.exit_button = QtWidgets.QPushButton(parent=Form)
        self.exit_button.setGeometry(QtCore.QRect(120, 160, 91, 23))
        self.exit_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.exit_button.setObjectName("exit_button")
        self.exit_button.clicked.connect(Form.close)

        # username label
        self.label_username = QtWidgets.QLabel(parent=Form)
        self.label_username.setGeometry(QtCore.QRect(20, 80, 71, 21))
        self.label_username.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.label_username.setObjectName("label_username")

        # password label
        self.label_password = QtWidgets.QLabel(parent=Form)
        self.label_password.setGeometry(QtCore.QRect(20, 120, 71, 20))
        self.label_password.setObjectName("label_password")

        # username input field
        self.edit_username = QtWidgets.QLineEdit(parent=Form)
        self.edit_username.setGeometry(QtCore.QRect(100, 80, 113, 20))
        self.edit_username.setObjectName("edit_username")

        # password input field
        self.edit_password = QtWidgets.QLineEdit(parent=Form)
        self.edit_password.setGeometry(QtCore.QRect(100, 120, 113, 20))
        self.edit_password.setObjectName("edit_password")
        self.edit_password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

        # information label
        self.label_information = QtWidgets.QLabel(parent=Form)
        self.label_information.setGeometry(QtCore.QRect(30, 190, 171, 21))
        self.label_information.setObjectName("label_information")

        # language combo box
        self.comboBox = QtWidgets.QComboBox(parent=Form)
        self.comboBox.setGeometry(QtCore.QRect(20, 30, 81, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("English")
        self.comboBox.addItem("Croatian")
        self.comboBox.addItem("French")
        self.comboBox.addItem("German")
        self.comboBox.addItem("Spanish")
        self.comboBox.activated.connect(lambda index: self.language_select(Form, self.comboBox.itemText(index), False))

        # language label
        self.label_language = QtWidgets.QLabel(parent=Form)
        self.label_language.setGeometry(QtCore.QRect(20, 10, 120, 21))
        self.label_language.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.label_language.setObjectName("label_language")

        # create new user button
        self.push_button_new_user = QtWidgets.QPushButton(parent=Form)
        self.push_button_new_user.setGeometry(QtCore.QRect(20, 240, 191, 24))
        self.push_button_new_user.setObjectName("push_button_new_user")
        self.push_button_new_user.clicked.connect(self.open_create_user_form)

        # open settings
        self.push_button_settings = QtWidgets.QPushButton(parent=Form)
        self.push_button_settings.setGeometry(QtCore.QRect(20, 280, 191, 24))
        self.push_button_settings.setObjectName("push_button_new_user")
        self.push_button_settings.clicked.connect(self.open_settings)
 
        self.language_select(Form, self.comboBox.currentText(), False)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
        self.win_reg_settings = win_reg_app_data()
        print(self.win_reg_settings)
        
        global only_once
        if only_once == True:
            only_once = False
            if self.win_reg_settings["default_language"] not in supported_languages:
                self.language_select(Form, "English", True)
            self.language_select(Form, self.win_reg_settings["default_language"], True)

    def open_create_user_form(self):
        self.main_window = QtWidgets.QMainWindow()
        self.create_user = Ui_Form()
        self.create_user.setupUi(self.main_window)
        self.main_window.show()
      
    def open_settings(self):
        pass 

    def login(self):
        if check_credentials(self.edit_username.text(), self.edit_password.text()):
            self.main_window = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self.main_window, self.comboBox.currentText(), self.edit_username.text())
            self.main_window.show()
            self.Form.close()
        else:
            QtWidgets.QMessageBox.warning(self.Form, "Login Failed", "Invalid username or password.")


    # localization
    def language_select(self, Form, language, from_winreg):
        if from_winreg == True:
            self.selected_language = language
        
        else:
            self.selected_language = self.comboBox.currentText()
            
        if self.selected_language == "French":
            _translate = QtCore.QCoreApplication.translate
            Form.setWindowTitle(_translate("Form", "Formulaire de connexion"))
            self.login_button.setText(_translate("Form", "Connexion"))
            self.exit_button.setText(_translate("Form", "Quitter"))
            self.label_username.setText(_translate("Form", "Nom d'utilisateur:"))
            self.label_password.setText(_translate("Form", "Mot de passe:"))
            self.label_information.setText(_translate("Form", "Entrez votre nom d'utilisateur et votre mot de passe"))
            self.label_language.setText(_translate("Form", "Sélectionnez votre langue:"))
            self.push_button_new_user.setText(_translate("Form", "Gestion des utilisateurs"))
            self.push_button_settings.setText(_translate("Form", "Paramètres"))

        if self.selected_language == "Croatian":
            _translate = QtCore.QCoreApplication.translate
            Form.setWindowTitle(_translate("Form", "Obrazac za prijavu"))
            self.login_button.setText(_translate("Form", "Prijava"))
            self.exit_button.setText(_translate("Form", "Izlaz"))
            self.label_username.setText(_translate("Form", "Korisničko ime:"))
            self.label_password.setText(_translate("Form", "Lozinka:"))
            self.label_information.setText(_translate("Form", "Unesite korisničko ime i lozinku"))
            self.label_language.setText(_translate("Form", "Odaberite jezik:"))
            self.push_button_new_user.setText(_translate("Form", "Upravljanje korisnicima"))
            self.push_button_settings.setText(_translate("Form", "Postavke"))
            
        if self.selected_language == "English":
            _translate = QtCore.QCoreApplication.translate
            Form.setWindowTitle(_translate("Form", "Form"))
            self.login_button.setText(_translate("Form", "Login"))
            self.exit_button.setText(_translate("Form", "Exit"))
            self.label_username.setText(_translate("Form", "Username:"))
            self.label_password.setText(_translate("Form", "Password:"))
            self.label_information.setText(_translate("Form", "Enter your username and password"))
            self.label_language.setText(_translate("Form", "Select your language:"))
            self.push_button_new_user.setText(_translate("Form", "User Management"))
            self.push_button_settings.setText(_translate("Form", "Settings"))


        if self.selected_language == "German":
            _translate = QtCore.QCoreApplication.translate
            Form.setWindowTitle(_translate("Form", "Formular"))
            self.login_button.setText(_translate("Form", "Anmelden"))
            self.exit_button.setText(_translate("Form", "Beenden"))
            self.label_username.setText(_translate("Form", "Benutzername:"))
            self.label_password.setText(_translate("Form", "Passwort:"))
            self.label_information.setText(_translate("Form", "Geben Sie Ihren Benutzernamen und Ihr Passwort ein"))
            self.label_language.setText(_translate("Form", "Wählen Sie Ihre Sprache:"))
            self.push_button_new_user.setText(_translate("Form", "Benutzerverwaltung"))
            self.push_button_settings.setText(_translate("Form", "Einstellungen"))

        if self.selected_language == "Spanish":
            _translate = QtCore.QCoreApplication.translate
            Form.setWindowTitle(_translate("Form", "Formulario"))
            self.login_button.setText(_translate("Form", "Iniciar sesión"))
            self.exit_button.setText(_translate("Form", "Salir"))
            self.label_username.setText(_translate("Form", "Usuario:"))
            self.label_password.setText(_translate("Form", "Contraseña:"))
            self.label_information.setText(_translate("Form", "Ingrese su nombre de usuario y contraseña"))
            self.label_language.setText(_translate("Form", "Seleccione su idioma:"))
            self.push_button_new_user.setText(_translate("Form", "Gestión de usuarios"))
            self.push_button_settings.setText(_translate("Form", "Configuración"))
