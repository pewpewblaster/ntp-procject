from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem
from PyQt6.QtCore import Qt
class CustomTableWidget(QTableWidget):
    def edit(self, index):
        # Override the edit() function to prevent editing
        if index.row() == self.rowCount() - 1 and index.column() == self.columnCount() - 1:
            return False  # Return False to disable editing
        else:
            return super().edit(index)  # Call the base class implementation for other cells

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a CustomTableWidget
        self.table_widget = CustomTableWidget(5, 5)
        self.setCentralWidget(self.table_widget)

        # Set the last cell as non-editable
        last_row = self.table_widget.rowCount() - 1
        last_column = self.table_widget.columnCount() - 1
        item = QTableWidgetItem("Last Cell")
        item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)  # Remove the ItemIsEditable flag
        self.table_widget.setItem(last_row, last_column, item)

        # Connect the cellClicked signal to a custom slot
        self.table_widget.cellClicked.connect(self.handle_cell_clicked)

    def handle_cell_clicked(self, row, column):
        if row == self.table_widget.rowCount() - 1 and column == self.table_widget.columnCount() - 1:
            # Only perform actions for the last cell
            item = self.table_widget.item(row, column)
            cell_text = item.text()
            print(f"Cell Clicked: {cell_text}")

app = QApplication([])
window = MainWindow()
window.show()
app.exec()
