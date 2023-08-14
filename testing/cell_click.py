import sys
import time
from PyQt6.QtCore import Qt, QThread, pyqtSignal, pyqtSlot, QObject
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget

class WorkerThread(QThread):
    update_signal = pyqtSignal(str)

    def run(self):
        for i in range(1, 6):
            time.sleep(1)
            self.update_signal.emit(f"Counter: {i}")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Threaded UI Update Demo")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.counter_button = QPushButton("Start Counter")
        self.counter_button.clicked.connect(self.start_counter)
        self.layout.addWidget(self.counter_button)

        self.counter_label = QPushButton("Counter: 0")
        self.layout.addWidget(self.counter_label)

    def start_counter(self):
        self.worker_thread = WorkerThread()
        self.worker_thread.update_signal.connect(self.update_counter_label)
        self.worker_thread.start()

    @pyqtSlot(str)
    def update_counter_label(self, value):
        self.counter_label.setText(value)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
