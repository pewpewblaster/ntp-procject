import sys
import json
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextBrowser, QLabel

class TextBrowserWidget(object):

    def setupUI(self):
        layout = QVBoxLayout()

        label1 = QLabel("Table Product Report", self)
        self.text_browser1 = QTextBrowser(self)

        label2 = QLabel("Table Warehouse-Product Report", self)
        self.text_browser2 = QTextBrowser(self)

        layout.addWidget(label1)
        layout.addWidget(self.text_browser1)
        layout.addWidget(label2)
        layout.addWidget(self.text_browser2)

        self.setLayout(layout)
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Text Browser Widget')

        # Example content for text browsers
        self.text_browser2.setPlainText("This is Text Browser 2.")

        # Display the dictionary in the first text browser
        data_dict = {
            "glossary": {
                "title": "example glossary",
                "GlossDiv": {
                    "title": "S",
                    "GlossList": {
                        "GlossEntry": {
                            "ID": "SGML",
                            "SortAs": "SGML",
                            "GlossTerm": "Standard Generalized Markup Language",
                            "Acronym": "SGML",
                            "Abbrev": "ISO 8879:1986",
                            "GlossDef": {
                                "para": "A meta-markup language, used to create markup languages such as DocBook.",
                                "GlossSeeAlso": ["GML", "XML"]
                            },
                            "GlossSee": "markup"
                        }
                    }
                }
            }
        }

        json_string = json.dumps(data_dict, indent=4)
        self.text_browser1.setPlainText(json_string)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TextBrowserWidget()
    window.show()
    sys.exit(app.exec())