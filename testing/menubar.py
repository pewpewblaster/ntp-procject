import sys
from PyQt6.QtWidgets import (
    QMainWindow, QApplication,
)
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtCore import Qt


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Menu Example')
        self.setGeometry(100, 100, 800, 600)

        self.actionShow_Report = QAction('Show Report', self)
        self.actionShow_Report.triggered.connect(lambda: print('Test'))  # Using a lambda function
        self.addAction(self.actionShow_Report)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
