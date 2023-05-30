import sys
from PyQt6.QtWidgets import QApplication, QWidget
from login_form import login_form
from PyQt6.QtGui import QFont, QPalette, QColor
import configparser

def settings(widget, config):
    font_name = config.get('Theme', 'font')
    font_size = int(config.get('Theme', 'font_size'))
    background_color = tuple(map(int, config.get('Theme', 'background_color').split(',')))

    font = QFont(font_name, font_size)
    widget.setFont(font)

    palette = QPalette()
    palette.setColor(QPalette.ColorRole.Window, QColor(*background_color))
    widget.setPalette(palette)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()

    config = configparser.ConfigParser()
    config.read('config/config.ini')

    settings(window, config)

    window.setGeometry(100, 100, 250, 300)
    
    login_window = login_form()
    login_window.login_ui(window)
    window.show()
    sys.exit(app.exec())
