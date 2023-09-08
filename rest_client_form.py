# Form implementation generated from reading ui file '.\rest_client.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import requests, json
from SQLite.sqlite3dll_handler_class import JwtDatabaseManager
from PyQt6.QtGui import QFont, QPalette, QColor


class Ui_rest_client(object):
    
    class RESTconnector():
        def __init__(self):
           self.rest_server_url = "https://nitroblaze.pythonanywhere.com/"
           # GET, only for admin user
           self.endpoint_protected = "api/protected"
           # POST and GET
           self.endpoint_logistic_partners = "api/logistic_partners"
        
        def get_protected_request(self, username):
            try:
                jwt_database = JwtDatabaseManager()
                token = jwt_database.get_jwt_for_username(username)
                # token = token_data.get("jwt_token")
                if token:
                    headers = {'Authorization': token}
                    response = requests.get(self.rest_server_url + self.endpoint_protected, 
                                            headers=headers, 
                                            verify=False)
                    print("Protected Response Content:", response.text)
                    return response.text
                else:
                    print("Error: Unable to extract JWT token from response.")
                    return None
            except requests.exceptions.ConnectionError:
                print("Connection to the REST server failed.")
        def get_endpoint_logistic_partners(self, username):
            try:
                jwt_database = JwtDatabaseManager()
                token = jwt_database.get_jwt_for_username(username)
                # token = token_data.get("jwt_token")
                if token:
                    headers = {'Authorization': token}
                    response = requests.get(self.rest_server_url + self.endpoint_logistic_partners, 
                                            headers=headers, 
                                            verify=False)
                    print("Protected Response Content:", response.text)
                    return response.text
                else:
                    print("Error: Unable to extract JWT token from response.")
                    return None
            except requests.exceptions.ConnectionError:
                print("Connection to the REST server failed.")
        
        def post_endpoint_logistic_partners(self, username, json_data):
            try:
                jwt_database = JwtDatabaseManager()
                token = jwt_database.get_jwt_for_username(username)
                
                if token:
                    headers = {'Authorization': token, 'Content-Type': 'application/json'}
                    response = requests.post(self.rest_server_url + self.endpoint_logistic_partners,
                                                headers=headers,
                                                json=json_data,  # Pass the JSON data as the request body
                                                verify=False)
                    
                    print("Response Content:", response.text)
                    return response.text
                else:
                    print("Error: Unable to extract JWT token from response.")
                    return None
            except requests.exceptions.ConnectionError:
                print("Connection to the REST server failed.")
                
    def setupUi(self,
                rest_client,
                username,
                language,
                app_settings):

        rest_client.setObjectName("rest_client")
        rest_client.setFixedSize(669, 442)
        self.rest_client = rest_client
        
        self.logged_user = username
        self.selected_language = language
        self.app_settings = app_settings
        
        
        """Application settings"""
        font = QFont(self.app_settings["font_name"],
                     self.app_settings["font_size"])
        self.rest_client.setFont(font)

        palette = QPalette()
        # font color
        palette.setColor(QPalette.ColorRole.WindowText,
                         QColor(*self.app_settings["font_color"]))
        # background color
        palette.setColor(QPalette.ColorRole.Window, 
                         QColor(*self.app_settings["background_color"]))
        self.rest_client.setPalette(palette)  
        
        self.textBrowser = QtWidgets.QTextBrowser(parent=rest_client)
        self.textBrowser.setGeometry(QtCore.QRect(20, 20, 331, 401))
        self.textBrowser.setObjectName("textBrowser")
        
        
        """ Groupbox logistic partners """
        self.groupBox_logistic_partners = QtWidgets.QGroupBox(parent=rest_client)
        self.groupBox_logistic_partners.setGeometry(QtCore.QRect(370, 20, 281, 261))
        self.groupBox_logistic_partners.setObjectName("groupBox_logistic_partners")
        # button show logistic partners
        self.pushButton_show_logistic_partners = QtWidgets.QPushButton(parent=self.groupBox_logistic_partners)
        self.pushButton_show_logistic_partners.setGeometry(QtCore.QRect(10, 20, 121, 23))
        self.pushButton_show_logistic_partners.setObjectName("pushButton_show_logistic_partners")
        self.pushButton_show_logistic_partners.clicked.connect(self.show_logistic_partners)
        # button add logistic partners
        self.pushButton_add_logistic_partners = QtWidgets.QPushButton(parent=self.groupBox_logistic_partners)
        self.pushButton_add_logistic_partners.setGeometry(QtCore.QRect(144, 20, 121, 23))
        self.pushButton_add_logistic_partners.setObjectName("pushButton_add_logistic_partners")
        self.pushButton_add_logistic_partners.clicked.connect(self.add_logistic_partners)
        
        self.label_partnert_name = QtWidgets.QLabel(parent=self.groupBox_logistic_partners)
        self.label_partnert_name.setGeometry(QtCore.QRect(16, 60, 251, 20))
        self.label_partnert_name.setObjectName("label_partnert_name")
        self.lineEdit_partner_name = QtWidgets.QLineEdit(parent=self.groupBox_logistic_partners)
        self.lineEdit_partner_name.setGeometry(QtCore.QRect(10, 80, 261, 20))
        self.lineEdit_partner_name.setObjectName("lineEdit_partner_name")
        self.label_address = QtWidgets.QLabel(parent=self.groupBox_logistic_partners)
        self.label_address.setGeometry(QtCore.QRect(16, 110, 251, 20))
        self.label_address.setObjectName("label_address")
        self.lineEdit_address = QtWidgets.QLineEdit(parent=self.groupBox_logistic_partners)
        self.lineEdit_address.setGeometry(QtCore.QRect(10, 130, 261, 20))
        self.lineEdit_address.setObjectName("lineEdit_address")
        self.lineEdit_contact_number = QtWidgets.QLineEdit(parent=self.groupBox_logistic_partners)
        self.lineEdit_contact_number.setGeometry(QtCore.QRect(10, 180, 261, 20))
        self.lineEdit_contact_number.setObjectName("lineEdit_contact_number")
        self.label_contact_number = QtWidgets.QLabel(parent=self.groupBox_logistic_partners)
        self.label_contact_number.setGeometry(QtCore.QRect(16, 160, 251, 20))
        self.label_contact_number.setObjectName("label_contact_number")
        self.label_contact_email = QtWidgets.QLabel(parent=self.groupBox_logistic_partners)
        self.label_contact_email.setGeometry(QtCore.QRect(16, 210, 251, 20))
        self.label_contact_email.setObjectName("label_contact_email")
        self.lineEdit_contact_email = QtWidgets.QLineEdit(parent=self.groupBox_logistic_partners)
        self.lineEdit_contact_email.setGeometry(QtCore.QRect(10, 230, 261, 20))
        self.lineEdit_contact_email.setObjectName("lineEdit_contact_email")
        
        """ Admin only """
        self.groupBox_admin_only = QtWidgets.QGroupBox(parent=rest_client)
        self.groupBox_admin_only.setGeometry(QtCore.QRect(370, 290, 271, 71))
        self.groupBox_admin_only.setObjectName("groupBox_admin_only")
        self.pushButton_admin_only = QtWidgets.QPushButton(parent=self.groupBox_admin_only)
        self.pushButton_admin_only.setGeometry(QtCore.QRect(10, 30, 251, 23))
        self.pushButton_admin_only.setObjectName("pushButton_admin_only")
        self.pushButton_admin_only.clicked.connect(self.rest_admin_only)
        self.retranslateUi(rest_client)
        QtCore.QMetaObject.connectSlotsByName(rest_client)

    def add_logistic_partners(self):
        update_json = {
            f"{self.lineEdit_partner_name.text()}" : {
                "address": f"{self.lineEdit_address.text()}",
                "contact_number": f"{self.lineEdit_contact_number.text()}",
                "contact_mail": f"{self.lineEdit_contact_email.text()}"        
            }  
        }
        try: 
            rest_conn = Ui_rest_client.RESTconnector()
            rest_server_value = rest_conn.post_endpoint_logistic_partners(self.logged_user, update_json)
            
            parsed_data = json.loads(rest_server_value)
            pretty_data = json.dumps(parsed_data, indent=4, sort_keys=True)
            self.textBrowser.setPlainText(pretty_data)       
        except json.JSONDecodeError as e:
            self.textBrowser.setPlainText(f"Error decoding JSON: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
                    

    def show_logistic_partners(self):
        rest_conn = Ui_rest_client.RESTconnector()
        rest_server_value = rest_conn.get_endpoint_logistic_partners(self.logged_user)
        
        try:
            parsed_data = json.loads(rest_server_value)
            pretty_data = json.dumps(parsed_data, indent=4, sort_keys=True)
            self.textBrowser.setPlainText(pretty_data)
        except json.JSONDecodeError as e:
            self.textBrowser.setPlainText(f"Error decoding JSON: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    
    def rest_admin_only(self):
        rest_conn = Ui_rest_client.RESTconnector()
        rest_server_value = rest_conn.get_protected_request(self.logged_user)
        
        try:
            parsed_data = json.loads(rest_server_value)
            pretty_data = json.dumps(parsed_data, indent=4, sort_keys=True)
            self.textBrowser.setPlainText(pretty_data)
        except json.JSONDecodeError as e:
            self.textBrowser.setPlainText(f"Error decoding JSON: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        
    def retranslateUi(self, rest_client):
        if self.selected_language == "English":
            _translate = QtCore.QCoreApplication.translate
            rest_client.setWindowTitle(_translate("rest_client", "Rest client"))
            self.groupBox_logistic_partners.setTitle(_translate("rest_client", "Logistic partners"))
            self.pushButton_show_logistic_partners.setText(_translate("rest_client", "Show"))
            self.pushButton_add_logistic_partners.setText(_translate("rest_client", "Add"))
            self.label_partnert_name.setText(_translate("rest_client", "Partner name"))
            self.label_address.setText(_translate("rest_client", "Address"))
            self.label_contact_number.setText(_translate("rest_client", "Contact number"))
            self.label_contact_email.setText(_translate("rest_client", "Contact e-mail"))
            self.groupBox_admin_only.setTitle(_translate("rest_client", "Admin only - show logistic API informations"))
            self.pushButton_admin_only.setText(_translate("rest_client", "Show"))

        if self.selected_language == "Croatian":
            _translate = QtCore.QCoreApplication.translate
            rest_client.setWindowTitle(_translate("rest_client", "REST klijent"))
            self.groupBox_logistic_partners.setTitle(_translate("rest_client", "Logistički partneri"))
            self.pushButton_show_logistic_partners.setText(_translate("rest_client", "Prikaži"))
            self.pushButton_add_logistic_partners.setText(_translate("rest_client", "Dodaj"))
            self.label_partnert_name.setText(_translate("rest_client", "Naziv partnera"))
            self.label_address.setText(_translate("rest_client", "Adresa"))
            self.label_contact_number.setText(_translate("rest_client", "Kontakt broj"))
            self.label_contact_email.setText(_translate("rest_client", "Kontakt e-pošta"))
            self.groupBox_admin_only.setTitle(_translate("rest_client", "Samo za administratore - prikaži informacije o logističkom API-ju"))
            self.pushButton_admin_only.setText(_translate("rest_client", "Prikaži"))
            
        if self.selected_language == "German":
            _translate = QtCore.QCoreApplication.translate
            rest_client.setWindowTitle(_translate("rest_client", "REST-Client"))
            self.groupBox_logistic_partners.setTitle(_translate("rest_client", "Logistikpartner"))
            self.pushButton_show_logistic_partners.setText(_translate("rest_client", "Anzeigen"))
            self.pushButton_add_logistic_partners.setText(_translate("rest_client", "Hinzufügen"))
            self.label_partnert_name.setText(_translate("rest_client", "Name des Partners"))
            self.label_address.setText(_translate("rest_client", "Adresse"))
            self.label_contact_number.setText(_translate("rest_client", "Kontaktnummer"))
            self.label_contact_email.setText(_translate("rest_client", "Kontakt-E-Mail"))
            self.groupBox_admin_only.setTitle(_translate("rest_client", "Nur für Administratoren - Zeige logistische API-Informationen"))
            self.pushButton_admin_only.setText(_translate("rest_client", "Anzeigen"))


        if self.selected_language == "Spanish":
            _translate = QtCore.QCoreApplication.translate
            rest_client.setWindowTitle(_translate("rest_client", "Cliente REST"))
            self.groupBox_logistic_partners.setTitle(_translate("rest_client", "Socios logísticos"))
            self.pushButton_show_logistic_partners.setText(_translate("rest_client", "Mostrar"))
            self.pushButton_add_logistic_partners.setText(_translate("rest_client", "Agregar"))
            self.label_partnert_name.setText(_translate("rest_client", "Nombre del socio"))
            self.label_address.setText(_translate("rest_client", "Dirección"))
            self.label_contact_number.setText(_translate("rest_client", "Número de contacto"))
            self.label_contact_email.setText(_translate("rest_client", "Correo electrónico de contacto"))
            self.groupBox_admin_only.setTitle(_translate("rest_client", "Solo para administradores - Mostrar información del API logístico"))
            self.pushButton_admin_only.setText(_translate("rest_client", "Mostrar"))


        if self.selected_language == "French":
            _translate = QtCore.QCoreApplication.translate
            rest_client.setWindowTitle(_translate("rest_client", "Client REST"))
            self.groupBox_logistic_partners.setTitle(_translate("rest_client", "Partenaires logistiques"))
            self.pushButton_show_logistic_partners.setText(_translate("rest_client", "Afficher"))
            self.pushButton_add_logistic_partners.setText(_translate("rest_client", "Ajouter"))
            self.label_partnert_name.setText(_translate("rest_client", "Nom du partenaire"))
            self.label_address.setText(_translate("rest_client", "Adresse"))
            self.label_contact_number.setText(_translate("rest_client", "Numéro de contact"))
            self.label_contact_email.setText(_translate("rest_client", "E-mail de contact"))
            self.groupBox_admin_only.setTitle(_translate("rest_client", "Réservé aux administrateurs - Afficher les informations de l'API logistique"))
            self.pushButton_admin_only.setText(_translate("rest_client", "Afficher"))
