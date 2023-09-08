from PyQt6 import QtCore, QtWidgets, QtGui
from PyQt6.QtGui import QFont, QPalette, QColor



class Ui_Form(object):
    def setupUi(self, Form,
                image_binary,
                language,
                app_settings):
    
        Form.setObjectName("Form")
        Form.resize(361, 481)
        self.form = Form
        self.app_settings = app_settings
        
        
        """Application settings"""
        font = QFont(self.app_settings["font_name"],
                     self.app_settings["font_size"])
        self.form.setFont(font)

        palette = QPalette()
        # font color
        palette.setColor(QPalette.ColorRole.WindowText,
                         QColor(*self.app_settings["font_color"]))
        # background color
        palette.setColor(QPalette.ColorRole.Window, 
                         QColor(*self.app_settings["background_color"]))
        self.form.setPalette(palette)   
        
        
        """ GUI """
        self.selected_language = language
        self.image_binary = image_binary
        
        self.grup_box_frame_show_Image = QtWidgets.QGroupBox(parent=Form)
        self.grup_box_frame_show_Image.setGeometry(QtCore.QRect(20, 10, 321, 421))
        self.grup_box_frame_show_Image.setObjectName("grup_box_frame_show_Image")
        
        self.frame_show_image = QtWidgets.QFrame(parent=self.grup_box_frame_show_Image)
        self.frame_show_image.setGeometry(QtCore.QRect(10, 20, 301, 391))
        self.frame_show_image.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_show_image.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_show_image.setObjectName("frame_show_image")
        
        self.label_image = QtWidgets.QLabel(self.frame_show_image)
        self.label_image.setGeometry(QtCore.QRect(0, 0, self.frame_show_image.width(), self.frame_show_image.height()))
        self.label_image.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_image.setObjectName("label_image")
        
        self.button_close_window = QtWidgets.QPushButton(parent=Form)
        self.button_close_window.setGeometry(QtCore.QRect(20, 440, 321, 23))
        self.button_close_window.setObjectName("button_close_window")
        self.button_close_window.clicked.connect(self.close_show_image_form)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.load_image()

    def load_image(self):
        # Convert the binary data to QImage
        qimage = QtGui.QImage.fromData(QtCore.QByteArray(self.image_binary))

        # Display the image in the label
        pixmap = QtGui.QPixmap.fromImage(qimage)
        scaled_pixmap = pixmap.scaled(self.label_image.size(), QtCore.Qt.AspectRatioMode.KeepAspectRatio, QtCore.Qt.TransformationMode.SmoothTransformation)
        self.label_image.setPixmap(scaled_pixmap)
    
    def close_show_image_form(self):
        # Close the window
        QtWidgets.QApplication.instance().activeWindow().close()
    
    def retranslateUi(self, Form):
        if self.selected_language == "English":
            _translate = QtCore.QCoreApplication.translate
            Form.setWindowTitle(_translate("Form", "Form"))
            self.grup_box_frame_show_Image.setTitle(_translate("Form", "Product image"))
            self.button_close_window.setText(_translate("Form", "Close"))
            
        if self.selected_language == "Croatian":
            _translate = QtCore.QCoreApplication.translate
            Form.setWindowTitle(_translate("Form", "Form"))
            self.grup_box_frame_show_Image.setTitle(_translate("Form", "Slika proizvoda"))
            self.button_close_window.setText(_translate("Form", "Zatvori"))
            
        if self.selected_language == "German":
            _translate = QtCore.QCoreApplication.translate
            Form.setWindowTitle(_translate("Form", "Form"))
            self.grup_box_frame_show_Image.setTitle(_translate("Form", "Produktbild"))
            self.button_close_window.setText(_translate("Form", "Schließen"))
            
        if self.selected_language == "Spanish":
            _translate = QtCore.QCoreApplication.translate
            Form.setWindowTitle(_translate("Form", "Formulario"))
            self.grup_box_frame_show_Image.setTitle(_translate("Form", "Imagen de producto"))
            self.button_close_window.setText(_translate("Form", "Cerrar"))
            
        if self.selected_language == "French":
            _translate = QtCore.QCoreApplication.translate
            Form.setWindowTitle(_translate("Form", "Formulaire"))
            self.grup_box_frame_show_Image.setTitle(_translate("Form", "Image du produit"))
            self.button_close_window.setText(_translate("Form", "Fermer"))




