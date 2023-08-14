import sys
import time
from PyQt6.QtCore import Qt, QThread, pyqtSignal
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget

class UIComponentRefresh(QThread):
    update_signal_time = pyqtSignal(str)
    update_signal_date = pyqtSignal(str)
    update_signal_refresh_time = pyqtSignal(str)
    update_signal_product_cost_sum = pyqtSignal(str)
    
    def __init__(self, custom_function):
        super().__init__()
        self.custom_function = custom_function

    def run(self):
        while True:
            current_time = time.strftime("%H:%M:%S")
            current_date = time.strftime("%Y-%m-%d")
            self.update_signal_time.emit(current_time)
            self.update_signal_date.emit(current_date)

            refresh_time = time.strftime("%H:%M:%S")
            self.update_signal_refresh_time.emit(refresh_time)
            
            if self.custom_function:
                custom_result = self.custom_function()
                self.update_signal_product_cost_sum.emit(custom_result)
                
            time.sleep(1)

def custom_processing():
    return "Custom processing result"

class MainForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("UI Component Refresh")
        self.setGeometry(100, 100, 400, 200)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout(central_widget)
        
        self.label_time_show = QLabel("Time will be updated...")
        self.label_date_show = QLabel("Date will be updated...")
        self.label_refresh_time_show = QLabel("Refresh time will be updated...")
        self.label_custom_show = QLabel("Custom processing result will be updated...")
        
        layout.addWidget(self.label_time_show, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label_date_show, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label_refresh_time_show, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label_custom_show, alignment=Qt.AlignmentFlag.AlignCenter)
        
        self.refresh_thread = UIComponentRefresh(custom_function=custom_processing)
        self.refresh_thread.update_signal_time.connect(self.update_time_label)
        self.refresh_thread.update_signal_date.connect(self.update_date_label)
        self.refresh_thread.update_signal_refresh_time.connect(self.update_refresh_time_label)
        self.refresh_thread.update_signal_product_cost_sum.connect(self.update_custom_label)
        self.refresh_thread.start()

    def update_time_label(self, new_time):
        self.label_time_show.setText(new_time)

    def update_date_label(self, new_date):
        self.label_date_show.setText(new_date)

    def update_refresh_time_label(self, new_refresh_time):
        self.label_refresh_time_show.setText(new_refresh_time)

    def update_custom_label(self, custom_result):
        self.label_custom_show.setText(custom_result)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainForm()
    window.show()
    sys.exit(app.exec())
