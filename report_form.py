import json
from PyQt6 import QtCore, QtWidgets
from datetime import datetime

class Report_Form(object):
    def setupUi(self, Form, product_data, master_detail_data, language):
        Form.setObjectName("Reprot Form")
        Form.resize(640, 801)
        
        self.selected_language = language
        self.product_data = product_data
        self.master_detail_data = master_detail_data
        
        self.label_product = QtWidgets.QLabel(parent=Form)
        self.label_product.setGeometry(QtCore.QRect(20, 10, 600, 31))
        self.label_product.setObjectName("label_product")
        self.textBrowser_product = QtWidgets.QTextBrowser(parent=Form)
        self.textBrowser_product.setGeometry(QtCore.QRect(20, 40, 601, 351))
        self.textBrowser_product.setObjectName("textBrowser_product")
        self.textBrowser_warehouse_product = QtWidgets.QTextBrowser(parent=Form)
        self.textBrowser_warehouse_product.setGeometry(QtCore.QRect(20, 430, 601, 351))
        self.textBrowser_warehouse_product.setObjectName("textBrowser_warehouse_product")
        self.label_warehouse_product = QtWidgets.QLabel(parent=Form)
        self.label_warehouse_product.setGeometry(QtCore.QRect(20, 400, 661, 31))
        self.label_warehouse_product.setObjectName("label_warehouse_product")

        # for both text browsers set scroll bar at the start/top
        self.textBrowser_warehouse_product.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        
        self.date_of_report = datetime.now().strftime('%Y-%m-%d')
        
        # for table "proizvodi"
        if isinstance(self.product_data, dict):
            
            self.total_amount_all_products = 0
            self.total_items = 0 
            self.total_products = 0 

            self.textBrowser_product.append("Izvjestaj iz baze podataka: 'skladiste.accdb', table: 'proizvodi'")
            self.textBrowser_product.append(f"Datum izvjestaja: {self.date_of_report}")
            self.textBrowser_product.append(f"---------------------------------------------------------\n")

            for product_key, product_value in self.product_data.items():
                
                self.total_items += 1
                
                product_category = product_value["kategorija"]
                product_price = product_value["cijena"]
                product_quantity = product_value["kolicina"]
                product_warehouse_id = product_value["skladiste_id"]
                
                self.total_amount_all_products += product_price * product_quantity
                self.total_products += product_quantity
                
                text_to_append = (
                    f"Naziv - {product_key}\n"
                    f"Kategorija - {product_category}\n"
                    f"Cijena - {product_price} kn\n"
                    f"Količina: {product_quantity}\n"
                    f"ID skladišta: {product_warehouse_id}\n"
                )
                self.textBrowser_product.append(text_to_append)
                
            self.textBrowser_product.append("---------------------------------------------------------")
            
            self.textBrowser_product.append(f"Ukupni iznos svih proizvoda iznosi: {self.total_amount_all_products} kn.")
            self.textBrowser_product.append(f"Ukupno stavki: {self.total_items}")
            self.textBrowser_product.append(f"Ukupno proizvoda: {self.total_products} kom")

        # for master-detail "skladista-proizvodi"
        if isinstance(self.master_detail_data, dict):
            
            self.total_amount_all_products= 0
            self.total_items = 0 
            self.total_products = 0

                            
            self.warehouse_total_amount_all_products = 0
            self.warehouse_total_items = 0 
            self.warehouse_total_products = 0
            
            self.textBrowser_warehouse_product.append("Izvjestaj za master-datel (skladiste->proizvodi)")
            self.textBrowser_warehouse_product.append(f"Datum izvjestaja: {self.date_of_report}")
            self.textBrowser_warehouse_product.append(f"---------------------------------------------------------\n")

            for skladiste_id, products in self.master_detail_data.items():
                self.textBrowser_warehouse_product.append(f"Skladiste ID: {skladiste_id}\n")
                for product in products:
                    product_name = product["naziv"]
                    product_category = product["kategorija"]
                    product_price = product["cijena"]
                    product_quantity = product["kolicina"]
                    product_warehouse_id = product["skladiste_id"]
                    attachment_text = "DA" if product["privitak"] == -1 else "NE"
                    
                    self.warehouse_total_items += 1
                    self.warehouse_total_amount_all_products += product_price * product_quantity
                    self.warehouse_total_products += product_quantity
                    
                    text_to_append = (
                        f"Naziv - {product_name}\n"
                        f"Kategorija - {product_category}\n"
                        f"Cijena - {product_price}\n"
                        f"Kolicina: {product_quantity}\n"
                        f"ID skladišta: {skladiste_id}\n"
                        f"Sadrzi privitak: {attachment_text}\n"
                    )
                    self.textBrowser_warehouse_product.append(text_to_append)
                    
                self.textBrowser_warehouse_product.append(f"\nStatistika za skladiste ID: {skladiste_id}")
                self.textBrowser_warehouse_product.append(f"Ukupni iznos svih proizvoda iznosi: {self.warehouse_total_amount_all_products} kn.")
                self.textBrowser_warehouse_product.append(f"Ukupno stavki: {self.warehouse_total_items}")
                self.textBrowser_warehouse_product.append(f"Ukupno proizvoda: {self.warehouse_total_products} kom\n")
                
                self.total_items += self.warehouse_total_items
                self.total_amount_all_products += self.warehouse_total_amount_all_products
                self.total_products += self.warehouse_total_products
                
                self.warehouse_total_amount_all_products = 0
                self.warehouse_total_items = 0 
                self.warehouse_total_products = 0
            
            self.textBrowser_warehouse_product.append("---------------------------------------------------------")              
            self.textBrowser_warehouse_product.append("Statistika za sva skladista:")
            self.textBrowser_warehouse_product.append(f"Ukupni iznos svih proizvoda iznosi: {self.total_amount_all_products} kn.")
            self.textBrowser_warehouse_product.append(f"Ukupno stavki: {self.total_items}")
            self.textBrowser_warehouse_product.append(f"Ukupno proizvoda: {self.total_products} kom")


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        if self.selected_language == "English":
            _translate = QtCore.QCoreApplication.translate
            Form.setWindowTitle(_translate("Form", "Form"))
            self.label_product.setText(_translate("Form", "Table Product report"))
            self.label_warehouse_product.setText(_translate("Form", "Table Warehouse-Product Report"))

        if self.selected_language == "Croatian":
            _translate = QtCore.QCoreApplication.translate
            Form.setWindowTitle(_translate("Form", "Obrazac"))
            self.label_product.setText(_translate("Form", "Izvješće o proizvodima"))
            self.label_warehouse_product.setText(_translate("Form", "Izvješće o skladištu i proizvodima"))
            
        if self.selected_language == "German":
            _translate = QtCore.QCoreApplication.translate
            Form.setWindowTitle(_translate("Form", "Formular"))
            self.label_product.setText(_translate("Form", "Produktbericht"))
            self.label_warehouse_product.setText(_translate("Form", "Lager-Produktbericht"))
            
        if self.selected_language == "Spanish":
            _translate = QtCore.QCoreApplication.translate
            Form.setWindowTitle(_translate("Form", "Formulario"))
            self.label_product.setText(_translate("Form", "Informe de Producto"))
            self.label_warehouse_product.setText(_translate("Form", "Informe de Almacén-Producto"))
            
        if self.selected_language == "French":
            _translate = QtCore.QCoreApplication.translate
            Form.setWindowTitle(_translate("Form", "Formulaire"))
            self.label_product.setText(_translate("Form", "Rapport de Produit"))
            self.label_warehouse_product.setText(_translate("Form", "Rapport d'Entrepôt-Produit"))


