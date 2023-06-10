import sys
from PyQt6.QtCore import Qt, QByteArray
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt6 import QtCore

class ImageForm(object):
    def login_form_Ui(self, image_data):
        # Create a label to display the image
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Set the central widget
        central_widget = QWidget(self)
        layout = QVBoxLayout(central_widget)
        layout.addWidget(self.image_label)
        self.setCentralWidget(central_widget)

        # Load and display the image
        self.load_image(image_data)
        
        QtCore.QMetaObject.connectSlotsByName(Form)

    
    def load_image(self, image_data):
        # Convert the binary data to QImage
        qimage = QImage.fromData(QByteArray(image_data))

        # Display the image in the label
        pixmap = QPixmap.fromImage(qimage)
        self.image_label.setPixmap(pixmap.scaledToWidth(800))

        # Resize the window to fit the image
        self.resize(pixmap.width(), pixmap.height())
        


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     form = ImageForm(get_image(4))
#     form.show()
#     sys.exit(app.exec())
