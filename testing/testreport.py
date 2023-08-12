from PyQt6.QtWidgets import QApplication, QMainWindow, QTextBrowser, QVBoxLayout, QWidget
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Product Data")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.text_browser_product = QTextBrowser()
        self.layout.addWidget(self.text_browser_product)

        self.master_detail_data = {
    "1": [
        {
            "skladiste_id": 1,
            "proizvod_id": 3,
            "naziv": "Sushi ",
            "cijena": 15,
            "kolicina": 3,
            "kategorija": "Hrana",
            "privitak": -1
        },
        {
            "skladiste_id": 1,
            "proizvod_id": 4,
            "naziv": "Pasta",
            "cijena": 7,
            "kolicina": 10,
            "kategorija": "Hrana",
            "privitak": -1
        },
        {
            "skladiste_id": 1,
            "proizvod_id": 8,
            "naziv": "Tipkovnica Logitech G413",
            "cijena": 50,
            "kolicina": 5,
            "kategorija": "Informatika",
            "privitak": 0
        }
    ],
    "4": [
        {
            "skladiste_id": 4,
            "proizvod_id": 9,
            "naziv": "Sushi",
            "cijena": 22,
            "kolicina": 7,
            "kategorija": "Hrana",
            "privitak": 0
        }
    ],
    "6": [
        {
            "skladiste_id": 6,
            "proizvod_id": 12,
            "naziv": "Biftek",
            "cijena": 20,
            "kolicina": 10,
            "kategorija": "Hrana",
            "privitak": 0
        }
    ]
}

        self.display_master_detail_data()


    def display_master_detail_data(self):
        for skladiste_id, products in self.master_detail_data.items():
            self.text_browser_product.append(f"Skladiste ID: {skladiste_id}\n")
            for product in products:
                naziv = product["naziv"]
                kategorija = product["kategorija"]
                cijena = product["cijena"]
                kolicina = product["kolicina"]
                skladiste_id = product["skladiste_id"]
                privitak = product["privitak"]
                
                privitak_text = "DA" if privitak == -1 else "NE"
                
                text_to_append = (
                    f"Naziv - {naziv}\n"
                    f"Kategorija - {kategorija}\n"
                    f"Cijena - {cijena}\n"
                    f"Količina: {kolicina}\n"
                    f"ID skladišta: {skladiste_id}\n"
                    f"Sadrzi privitak: {privitak} privitak: {privitak_text}\n\n"
                )
                self.text_browser_product.append(text_to_append)

app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())
