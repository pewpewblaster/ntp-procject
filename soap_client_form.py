# Form implementation generated from reading ui file '.\soap_client.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtWidgets, QtGui
import requests


class Ui_soap_client(object):
    
    class SOAP_request():
        def __init__(self, country_code):
            self.country_code = country_code
            self.request_url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"
            self.response_status_code = None
            self.response = None
            self.payload = f"""<?xml version=\"1.0\" encoding=\"utf-8\"?>
            <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
              <soap:Body>
                <CountryCurrency xmlns="http://www.oorsprong.org/websamples.countryinfo">
                  <sCountryISOCode>{self.country_code }</sCountryISOCode>
                </CountryCurrency>
              </soap:Body>
            </soap:Envelope>"""
        
        def get_request(self):
            
            self.headers = {
            'Content-Type': 'text/xml; charset=utf-8'
            }
            print("Debug")
            print(self.request_url)
            print(self.headers)
            print(self.payload)
            self.response = requests.request("POST", self.request_url, headers=self.headers, data=self.payload)
            self.response_status_code = self.response.status_code
            
        def return_request_data(self):
            return self.response.text, self.response_status_code
            
    def setupUi(self, soap_client):
        soap_client.setObjectName("soap_client")
        soap_client.setFixedSize(707, 377)
        
        self.list_country_codes = [
            "Croatia - HR",
            "United States - US",
            "Canada - CA",
            "Australia - AU",
            "Great Britain - GB",
            "China - CN",
            "Japan - JP",
            "Germany - DE",
            "India - IN",
            "France - FR",
            "Brazil - BR",
            "Italy - IT",
            "South Korea - KR",
            "Russia - RU",
            "Spain - ES",
            "Mexico - MX",
            "Indonesia - ID",
            "Netherlands - NL",
            "Saudi Arabia - SA",
            "Turkey - TR",
            "Switzerland - CH"
        ]
                
        
        """ Country Codes """
        self.listWidget_country_codes = QtWidgets.QListWidget(parent=soap_client)
        self.listWidget_country_codes.setGeometry(QtCore.QRect(20, 30, 151, 192))
        self.listWidget_country_codes.setObjectName("listView_country_codes")
        
        for codes in self.list_country_codes:
            self.listWidget_country_codes.addItem(codes)
        self.listWidget_country_codes.itemClicked.connect(self.select_country_code)

        self.label_country_codes = QtWidgets.QLabel(parent=soap_client)
        self.label_country_codes.setGeometry(QtCore.QRect(20, 10, 151, 16))
        self.label_country_codes.setObjectName("label_country_codes")
        self.label_enter_country_code = QtWidgets.QLabel(parent=soap_client)
        self.label_enter_country_code.setGeometry(QtCore.QRect(20, 236, 151, 20))
        self.label_enter_country_code.setObjectName("label_enter_country_code")
        self.lineEdit_enter_country_code = QtWidgets.QLineEdit(parent=soap_client)
        self.lineEdit_enter_country_code.setGeometry(QtCore.QRect(20, 260, 151, 20))
        self.lineEdit_enter_country_code.setObjectName("lineEdit_enter_country_code")
        self.pushButton_send_request = QtWidgets.QPushButton(parent=soap_client)
        self.pushButton_send_request.setGeometry(QtCore.QRect(20, 290, 151, 23))
        self.pushButton_send_request.setObjectName("pushButton_send_request")
        self.pushButton_send_request.clicked.connect(self.send_soap_request)
        
        """ SOAP message textbox """
        self.textBrowser_soap_message = QtWidgets.QTextBrowser(parent=soap_client)
        self.textBrowser_soap_message.setGeometry(QtCore.QRect(190, 30, 491, 192))
        self.textBrowser_soap_message.setObjectName("textBrowser_soap_message")
        self.label_request_code = QtWidgets.QLabel(parent=soap_client)
        self.label_request_code.setGeometry(QtCore.QRect(200, 230, 81, 16))
        self.label_request_code.setObjectName("label_request_code")
        self.label_show_request_code = QtWidgets.QLabel(parent=soap_client)
        self.label_show_request_code.setGeometry(QtCore.QRect(290, 230, 61, 16))
        self.label_show_request_code.setObjectName("label_show_request_code")
        self.label = QtWidgets.QLabel(parent=soap_client)
        self.label.setGeometry(QtCore.QRect(190, 10, 491, 16))
        self.label.setObjectName("label")

        self.retranslateUi(soap_client)
        QtCore.QMetaObject.connectSlotsByName(soap_client)

    
    def select_country_code(self, item):
        # gets the index of the clicked item on the 
        clicked_index = self.listWidget_country_codes.row(item)  # Get the index of the clicked item
        # splits string into 2 strings and returns the second one (country code)
        country_code = self.list_country_codes[clicked_index].split(" - ")[1]
        self.lineEdit_enter_country_code.setText(country_code)    
    
    def send_soap_request(self):
        self.soap_client = Ui_soap_client.SOAP_request(self.lineEdit_enter_country_code.text())
        self.soap_client.get_request()
        
        self.soap_message, self.soap_status_code = self.soap_client.return_request_data()
        
        self.label_show_request_code.setText(str(self.soap_status_code))
        self.textBrowser_soap_message.append(self.soap_message)
        
        
    def retranslateUi(self, soap_client):
        _translate = QtCore.QCoreApplication.translate
        soap_client.setWindowTitle(_translate("soap_client", "SOAP client"))
        self.label_country_codes.setText(_translate("soap_client", "Country codes:"))
        self.label_enter_country_code.setText(_translate("soap_client", "Enter country code:"))
        self.pushButton_send_request.setText(_translate("soap_client", "Send request"))
        self.label_request_code.setText(_translate("soap_client", "Status code:"))
        self.label_show_request_code.setText(_translate("soap_client", "None"))
        self.label.setText(_translate("soap_client", "SOAP message:"))
