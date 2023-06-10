from PyQt6 import QtCore, QtWidgets, QtGui


class Ui_Form(object):
    def setupUi(self, Form, image_binary):
        Form.setObjectName("Form")
        Form.resize(361, 481)
        
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
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.grup_box_frame_show_Image.setTitle(_translate("Form", "GroupBox"))
        self.button_close_window.setText(_translate("Form", "Close"))




