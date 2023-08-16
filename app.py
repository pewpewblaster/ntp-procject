import sys
from PyQt6.QtWidgets import QApplication, QWidget
from login_form import login_form
from PyQt6.QtGui import QFont, QPalette, QColor
import configparser
from winreg_utils import win_reg_app_data

'''glbal variables'''

''' classes '''
class ApplicationSettings:
    def __init__(self, widget, config):
        self.widget = widget
        self.config = config
        self.font_name = None
        self.font_size = None
        self.background_color = None
        self.font = None

    def apply_settings(self):
        self.font_name = self.config.get('Theme', 'font')
        self.font_size = int(self.config.get('Theme', 'font_size'))
        self.background_color = tuple(map(int, self.config.get('Theme', 'background_color').split(',')))
        palette = QPalette()
        data_from_win_reg = win_reg_app_data()

        # Get font color from the data_from_win_reg dictionary
        font_color = tuple(map(int, data_from_win_reg['font_color'].split(',')))
        print(font_color)
        palette.setColor(QPalette.ColorRole.WindowText, QColor(*font_color))
        
        self.widget.setPalette(palette)
        
        font = QFont(self.font_name, self.font_size)
        self.widget.setFont(font)
        
        # Set widget geometry from the data_from_win_reg dictionary
        geometry_values = list(map(int, data_from_win_reg['geometry'].split(',')))
        self.widget.setGeometry(geometry_values[0], geometry_values[1], geometry_values[2], geometry_values[3])

        
        palette.setColor(QPalette.ColorRole.Window, QColor(*self.background_color))
        self.widget.setPalette(palette)
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()

    config = configparser.ConfigParser()
    config.read('config/config.ini')

    app_settings = ApplicationSettings(window, config)
    app_settings.apply_settings()

    # window.setGeometry(100, 100, 250, 320)

    login_window = login_form()
    login_window.login_ui(window)
    window.show()

    sys.exit(app.exec())
