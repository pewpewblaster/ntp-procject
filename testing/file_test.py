import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a QLabel widget to display the image
        self.image_label = QLabel(self)
        self.setCentralWidget(self.image_label)

        # Set the image
        current_directory = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(current_directory, "image.jpg")
        self.set_image(image_path)

    def set_image(self, image_path):
        # Load the image using QPixmap
        pixmap = QPixmap(image_path)

        # Check if the image was loaded successfully
        if pixmap.isNull():
            print("Error loading image")
            return

        # Set the pixmap as the content of the QLabel
        self.image_label.setPixmap(pixmap)
        self.image_label.setScaledContents(True)  # Scale the image to fit the label

app = QApplication([])
window = MainWindow()
window.show()
app.exec()
