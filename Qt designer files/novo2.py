# Form implementation generated from reading ui file 'database_view_window.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1304, 872)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.table_proizvodi = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.table_proizvodi.setGeometry(QtCore.QRect(30, 410, 691, 201))
        self.table_proizvodi.setObjectName("table_proizvodi")
        self.table_proizvodi.setColumnCount(0)
        self.table_proizvodi.setRowCount(0)
        self.group_box_information = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.group_box_information.setGeometry(QtCore.QRect(10, 10, 311, 71))
        self.group_box_information.setObjectName("group_box_information")
        self.label_active_language_show = QtWidgets.QLabel(parent=self.group_box_information)
        self.label_active_language_show.setGeometry(QtCore.QRect(80, 40, 47, 21))
        self.label_active_language_show.setObjectName("label_active_language_show")
        self.label_active_user = QtWidgets.QLabel(parent=self.group_box_information)
        self.label_active_user.setGeometry(QtCore.QRect(10, 20, 61, 21))
        self.label_active_user.setObjectName("label_active_user")
        self.label_active_user_show = QtWidgets.QLabel(parent=self.group_box_information)
        self.label_active_user_show.setGeometry(QtCore.QRect(80, 20, 47, 21))
        self.label_active_user_show.setObjectName("label_active_user_show")
        self.label_active_language = QtWidgets.QLabel(parent=self.group_box_information)
        self.label_active_language.setGeometry(QtCore.QRect(10, 40, 61, 21))
        self.label_active_language.setObjectName("label_active_language")
        self.label_date = QtWidgets.QLabel(parent=self.group_box_information)
        self.label_date.setGeometry(QtCore.QRect(180, 20, 31, 21))
        self.label_date.setObjectName("label_date")
        self.label_time_show = QtWidgets.QLabel(parent=self.group_box_information)
        self.label_time_show.setGeometry(QtCore.QRect(220, 40, 71, 21))
        self.label_time_show.setObjectName("label_time_show")
        self.label_date_show = QtWidgets.QLabel(parent=self.group_box_information)
        self.label_date_show.setGeometry(QtCore.QRect(220, 20, 71, 21))
        self.label_date_show.setObjectName("label_date_show")
        self.label_time = QtWidgets.QLabel(parent=self.group_box_information)
        self.label_time.setGeometry(QtCore.QRect(180, 40, 31, 21))
        self.label_time.setObjectName("label_time")
        self.group_box_selected_warehouse = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.group_box_selected_warehouse.setGeometry(QtCore.QRect(10, 100, 300, 243))
        self.group_box_selected_warehouse.setObjectName("group_box_selected_warehouse")
        self.label_warehouse_information_id = QtWidgets.QLabel(parent=self.group_box_selected_warehouse)
        self.label_warehouse_information_id.setGeometry(QtCore.QRect(20, 40, 111, 16))
        self.label_warehouse_information_id.setObjectName("label_warehouse_information_id")
        self.label_warehouse_information_id_show = QtWidgets.QLabel(parent=self.group_box_selected_warehouse)
        self.label_warehouse_information_id_show.setGeometry(QtCore.QRect(140, 40, 141, 16))
        self.label_warehouse_information_id_show.setObjectName("label_warehouse_information_id_show")
        self.label_warehouse_information_name = QtWidgets.QLabel(parent=self.group_box_selected_warehouse)
        self.label_warehouse_information_name.setGeometry(QtCore.QRect(20, 60, 111, 16))
        self.label_warehouse_information_name.setObjectName("label_warehouse_information_name")
        self.label_warehouse_information_name_show = QtWidgets.QLabel(parent=self.group_box_selected_warehouse)
        self.label_warehouse_information_name_show.setGeometry(QtCore.QRect(140, 60, 141, 16))
        self.label_warehouse_information_name_show.setObjectName("label_warehouse_information_name_show")
        self.label_warehouse_information_street_show = QtWidgets.QLabel(parent=self.group_box_selected_warehouse)
        self.label_warehouse_information_street_show.setGeometry(QtCore.QRect(140, 80, 131, 16))
        self.label_warehouse_information_street_show.setObjectName("label_warehouse_information_street_show")
        self.label_warehouse_information_city_show = QtWidgets.QLabel(parent=self.group_box_selected_warehouse)
        self.label_warehouse_information_city_show.setGeometry(QtCore.QRect(140, 100, 131, 16))
        self.label_warehouse_information_city_show.setObjectName("label_warehouse_information_city_show")
        self.label_warehouse_information_city = QtWidgets.QLabel(parent=self.group_box_selected_warehouse)
        self.label_warehouse_information_city.setGeometry(QtCore.QRect(20, 100, 111, 16))
        self.label_warehouse_information_city.setObjectName("label_warehouse_information_city")
        self.label_warehouse_information_street = QtWidgets.QLabel(parent=self.group_box_selected_warehouse)
        self.label_warehouse_information_street.setGeometry(QtCore.QRect(20, 80, 111, 16))
        self.label_warehouse_information_street.setObjectName("label_warehouse_information_street")
        self.label_warehouse_information_country_show = QtWidgets.QLabel(parent=self.group_box_selected_warehouse)
        self.label_warehouse_information_country_show.setGeometry(QtCore.QRect(140, 120, 141, 16))
        self.label_warehouse_information_country_show.setObjectName("label_warehouse_information_country_show")
        self.label_warehouse_information_country = QtWidgets.QLabel(parent=self.group_box_selected_warehouse)
        self.label_warehouse_information_country.setGeometry(QtCore.QRect(20, 120, 111, 16))
        self.label_warehouse_information_country.setObjectName("label_warehouse_information_country")
        self.push_button_select_warehouse = QtWidgets.QPushButton(parent=self.group_box_selected_warehouse)
        self.push_button_select_warehouse.setGeometry(QtCore.QRect(20, 180, 151, 23))
        self.push_button_select_warehouse.setObjectName("push_button_select_warehouse")
        self.line_edit_select_warehouse = QtWidgets.QLineEdit(parent=self.group_box_selected_warehouse)
        self.line_edit_select_warehouse.setGeometry(QtCore.QRect(20, 150, 151, 20))
        self.line_edit_select_warehouse.setObjectName("line_edit_select_warehouse")
        self.table_show_warehouse_products = QtWidgets.QTableView(parent=self.centralwidget)
        self.table_show_warehouse_products.setGeometry(QtCore.QRect(750, 410, 531, 201))
        self.table_show_warehouse_products.setObjectName("table_show_warehouse_products")
        self.button_show_products = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_show_products.setGeometry(QtCore.QRect(750, 370, 251, 23))
        self.button_show_products.setObjectName("button_show_products")
        self.button_show_warehouses = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_show_warehouses.setGeometry(QtCore.QRect(1030, 370, 251, 23))
        self.button_show_warehouses.setObjectName("button_show_warehouses")
        self.button_find_warehouse_by_product = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_find_warehouse_by_product.setGeometry(QtCore.QRect(40, 370, 91, 23))
        self.button_find_warehouse_by_product.setObjectName("button_find_warehouse_by_product")
        self.edit_find_warehouse_by_product = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.edit_find_warehouse_by_product.setGeometry(QtCore.QRect(140, 370, 181, 20))
        self.edit_find_warehouse_by_product.setObjectName("edit_find_warehouse_by_product")
        self.group_delete_warehouse_product = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.group_delete_warehouse_product.setGeometry(QtCore.QRect(970, 100, 300, 241))
        self.group_delete_warehouse_product.setObjectName("group_delete_warehouse_product")
        self.label_delete_warehouse = QtWidgets.QLabel(parent=self.group_delete_warehouse_product)
        self.label_delete_warehouse.setGeometry(QtCore.QRect(20, 40, 261, 20))
        self.label_delete_warehouse.setObjectName("label_delete_warehouse")
        self.label_delete_products = QtWidgets.QLabel(parent=self.group_delete_warehouse_product)
        self.label_delete_products.setGeometry(QtCore.QRect(20, 140, 261, 20))
        self.label_delete_products.setObjectName("label_delete_products")
        self.button_delete_warehouse = QtWidgets.QPushButton(parent=self.group_delete_warehouse_product)
        self.button_delete_warehouse.setGeometry(QtCore.QRect(20, 100, 251, 23))
        self.button_delete_warehouse.setObjectName("button_delete_warehouse")
        self.edit_delete_warehouse = QtWidgets.QLineEdit(parent=self.group_delete_warehouse_product)
        self.edit_delete_warehouse.setGeometry(QtCore.QRect(20, 70, 251, 20))
        self.edit_delete_warehouse.setObjectName("edit_delete_warehouse")
        self.edit_delete_products = QtWidgets.QLineEdit(parent=self.group_delete_warehouse_product)
        self.edit_delete_products.setGeometry(QtCore.QRect(20, 170, 251, 20))
        self.edit_delete_products.setObjectName("edit_delete_products")
        self.button_delete_product = QtWidgets.QPushButton(parent=self.group_delete_warehouse_product)
        self.button_delete_product.setGeometry(QtCore.QRect(20, 200, 251, 23))
        self.button_delete_product.setObjectName("button_delete_product")
        self.tab_warehouse = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tab_warehouse.setGeometry(QtCore.QRect(330, 90, 300, 251))
        self.tab_warehouse.setObjectName("tab_warehouse")
        self.tab_add_warehouse = QtWidgets.QWidget()
        self.tab_add_warehouse.setObjectName("tab_add_warehouse")
        self.line_edit_warehoue_city = QtWidgets.QLineEdit(parent=self.tab_add_warehouse)
        self.line_edit_warehoue_city.setGeometry(QtCore.QRect(130, 80, 151, 20))
        self.line_edit_warehoue_city.setObjectName("line_edit_warehoue_city")
        self.label_warehouse_city = QtWidgets.QLabel(parent=self.tab_add_warehouse)
        self.label_warehouse_city.setGeometry(QtCore.QRect(20, 80, 101, 20))
        self.label_warehouse_city.setObjectName("label_warehouse_city")
        self.label_warehouse_street = QtWidgets.QLabel(parent=self.tab_add_warehouse)
        self.label_warehouse_street.setGeometry(QtCore.QRect(20, 50, 101, 21))
        self.label_warehouse_street.setObjectName("label_warehouse_street")
        self.label_warehouse_name = QtWidgets.QLabel(parent=self.tab_add_warehouse)
        self.label_warehouse_name.setGeometry(QtCore.QRect(20, 20, 101, 20))
        self.label_warehouse_name.setObjectName("label_warehouse_name")
        self.line_edit_warehoue_street = QtWidgets.QLineEdit(parent=self.tab_add_warehouse)
        self.line_edit_warehoue_street.setGeometry(QtCore.QRect(130, 50, 151, 20))
        self.line_edit_warehoue_street.setObjectName("line_edit_warehoue_street")
        self.button_save_warehouse = QtWidgets.QPushButton(parent=self.tab_add_warehouse)
        self.button_save_warehouse.setGeometry(QtCore.QRect(20, 150, 261, 23))
        self.button_save_warehouse.setObjectName("button_save_warehouse")
        self.line_edit_warehoue_name = QtWidgets.QLineEdit(parent=self.tab_add_warehouse)
        self.line_edit_warehoue_name.setGeometry(QtCore.QRect(130, 20, 151, 20))
        self.line_edit_warehoue_name.setObjectName("line_edit_warehoue_name")
        self.label_warehouse_country = QtWidgets.QLabel(parent=self.tab_add_warehouse)
        self.label_warehouse_country.setGeometry(QtCore.QRect(20, 110, 101, 20))
        self.label_warehouse_country.setObjectName("label_warehouse_country")
        self.line_edit_warehoue_country = QtWidgets.QLineEdit(parent=self.tab_add_warehouse)
        self.line_edit_warehoue_country.setGeometry(QtCore.QRect(130, 110, 151, 20))
        self.line_edit_warehoue_country.setObjectName("line_edit_warehoue_country")
        self.tab_warehouse.addTab(self.tab_add_warehouse, "")
        self.tab_edit_warehouse = QtWidgets.QWidget()
        self.tab_edit_warehouse.setObjectName("tab_edit_warehouse")
        self.label_warehouse_city_edit = QtWidgets.QLabel(parent=self.tab_edit_warehouse)
        self.label_warehouse_city_edit.setGeometry(QtCore.QRect(20, 100, 101, 20))
        self.label_warehouse_city_edit.setObjectName("label_warehouse_city_edit")
        self.label_warehouse_street_edit = QtWidgets.QLabel(parent=self.tab_edit_warehouse)
        self.label_warehouse_street_edit.setGeometry(QtCore.QRect(20, 70, 101, 21))
        self.label_warehouse_street_edit.setObjectName("label_warehouse_street_edit")
        self.label_warehouse_name_edit = QtWidgets.QLabel(parent=self.tab_edit_warehouse)
        self.label_warehouse_name_edit.setGeometry(QtCore.QRect(20, 40, 101, 20))
        self.label_warehouse_name_edit.setObjectName("label_warehouse_name_edit")
        self.button_edit_warehouse = QtWidgets.QPushButton(parent=self.tab_edit_warehouse)
        self.button_edit_warehouse.setGeometry(QtCore.QRect(20, 170, 261, 23))
        self.button_edit_warehouse.setObjectName("button_edit_warehouse")
        self.line_edit_warehoue_city_edit = QtWidgets.QLineEdit(parent=self.tab_edit_warehouse)
        self.line_edit_warehoue_city_edit.setGeometry(QtCore.QRect(130, 100, 151, 20))
        self.line_edit_warehoue_city_edit.setObjectName("line_edit_warehoue_city_edit")
        self.line_edit_warehoue_street_edit = QtWidgets.QLineEdit(parent=self.tab_edit_warehouse)
        self.line_edit_warehoue_street_edit.setGeometry(QtCore.QRect(130, 70, 151, 20))
        self.line_edit_warehoue_street_edit.setObjectName("line_edit_warehoue_street_edit")
        self.line_edit_warehoue_name_edit = QtWidgets.QLineEdit(parent=self.tab_edit_warehouse)
        self.line_edit_warehoue_name_edit.setGeometry(QtCore.QRect(130, 40, 151, 20))
        self.line_edit_warehoue_name_edit.setObjectName("line_edit_warehoue_name_edit")
        self.label_warehouse_country_edit = QtWidgets.QLabel(parent=self.tab_edit_warehouse)
        self.label_warehouse_country_edit.setGeometry(QtCore.QRect(20, 130, 101, 20))
        self.label_warehouse_country_edit.setObjectName("label_warehouse_country_edit")
        self.line_edit_warehoue_country_edit = QtWidgets.QLineEdit(parent=self.tab_edit_warehouse)
        self.line_edit_warehoue_country_edit.setGeometry(QtCore.QRect(130, 130, 151, 20))
        self.line_edit_warehoue_country_edit.setObjectName("line_edit_warehoue_country_edit")
        self.label_warehouse_id_edit = QtWidgets.QLabel(parent=self.tab_edit_warehouse)
        self.label_warehouse_id_edit.setGeometry(QtCore.QRect(20, 10, 101, 20))
        self.label_warehouse_id_edit.setObjectName("label_warehouse_id_edit")
        self.line_edit_warehoue_name_id_edit = QtWidgets.QLineEdit(parent=self.tab_edit_warehouse)
        self.line_edit_warehoue_name_id_edit.setGeometry(QtCore.QRect(130, 10, 151, 20))
        self.line_edit_warehoue_name_id_edit.setObjectName("line_edit_warehoue_name_id_edit")
        self.tab_warehouse.addTab(self.tab_edit_warehouse, "")
        self.tab_products = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tab_products.setGeometry(QtCore.QRect(650, 90, 300, 251))
        self.tab_products.setObjectName("tab_products")
        self.tab_add_product = QtWidgets.QWidget()
        self.tab_add_product.setObjectName("tab_add_product")
        self.line_edit_products_warehouse_id = QtWidgets.QLineEdit(parent=self.tab_add_product)
        self.line_edit_products_warehouse_id.setGeometry(QtCore.QRect(100, 20, 181, 20))
        self.line_edit_products_warehouse_id.setObjectName("line_edit_products_warehouse_id")
        self.label_product_warehouse_id = QtWidgets.QLabel(parent=self.tab_add_product)
        self.label_product_warehouse_id.setGeometry(QtCore.QRect(20, 20, 71, 20))
        self.label_product_warehouse_id.setObjectName("label_product_warehouse_id")
        self.line_edit_products_quantity = QtWidgets.QLineEdit(parent=self.tab_add_product)
        self.line_edit_products_quantity.setGeometry(QtCore.QRect(100, 110, 181, 20))
        self.line_edit_products_quantity.setObjectName("line_edit_products_quantity")
        self.line_edit_products_category = QtWidgets.QLineEdit(parent=self.tab_add_product)
        self.line_edit_products_category.setGeometry(QtCore.QRect(100, 140, 181, 20))
        self.line_edit_products_category.setObjectName("line_edit_products_category")
        self.label_product_name = QtWidgets.QLabel(parent=self.tab_add_product)
        self.label_product_name.setGeometry(QtCore.QRect(20, 50, 71, 21))
        self.label_product_name.setObjectName("label_product_name")
        self.label_product_quantity = QtWidgets.QLabel(parent=self.tab_add_product)
        self.label_product_quantity.setGeometry(QtCore.QRect(20, 110, 71, 21))
        self.label_product_quantity.setScaledContents(False)
        self.label_product_quantity.setWordWrap(False)
        self.label_product_quantity.setObjectName("label_product_quantity")
        self.line_edit_products_name = QtWidgets.QLineEdit(parent=self.tab_add_product)
        self.line_edit_products_name.setGeometry(QtCore.QRect(100, 50, 181, 20))
        self.line_edit_products_name.setObjectName("line_edit_products_name")
        self.button_save_product = QtWidgets.QPushButton(parent=self.tab_add_product)
        self.button_save_product.setGeometry(QtCore.QRect(20, 170, 261, 23))
        self.button_save_product.setObjectName("button_save_product")
        self.line_edit_products_price = QtWidgets.QLineEdit(parent=self.tab_add_product)
        self.line_edit_products_price.setGeometry(QtCore.QRect(100, 80, 181, 20))
        self.line_edit_products_price.setObjectName("line_edit_products_price")
        self.label_product_category = QtWidgets.QLabel(parent=self.tab_add_product)
        self.label_product_category.setGeometry(QtCore.QRect(20, 140, 71, 21))
        self.label_product_category.setScaledContents(False)
        self.label_product_category.setWordWrap(False)
        self.label_product_category.setObjectName("label_product_category")
        self.label_product_price = QtWidgets.QLabel(parent=self.tab_add_product)
        self.label_product_price.setGeometry(QtCore.QRect(20, 80, 71, 21))
        self.label_product_price.setObjectName("label_product_price")
        self.tab_products.addTab(self.tab_add_product, "")
        self.tab_edit_product = QtWidgets.QWidget()
        self.tab_edit_product.setObjectName("tab_edit_product")
        self.label_product_name_edit = QtWidgets.QLabel(parent=self.tab_edit_product)
        self.label_product_name_edit.setGeometry(QtCore.QRect(20, 70, 71, 21))
        self.label_product_name_edit.setObjectName("label_product_name_edit")
        self.label_product_price_edit = QtWidgets.QLabel(parent=self.tab_edit_product)
        self.label_product_price_edit.setGeometry(QtCore.QRect(20, 100, 71, 21))
        self.label_product_price_edit.setObjectName("label_product_price_edit")
        self.label_product_warehouse_id_edit = QtWidgets.QLabel(parent=self.tab_edit_product)
        self.label_product_warehouse_id_edit.setGeometry(QtCore.QRect(20, 40, 71, 20))
        self.label_product_warehouse_id_edit.setObjectName("label_product_warehouse_id_edit")
        self.label_product_quantity_edit = QtWidgets.QLabel(parent=self.tab_edit_product)
        self.label_product_quantity_edit.setGeometry(QtCore.QRect(20, 130, 71, 21))
        self.label_product_quantity_edit.setScaledContents(False)
        self.label_product_quantity_edit.setWordWrap(False)
        self.label_product_quantity_edit.setObjectName("label_product_quantity_edit")
        self.line_edit_products_price_edit = QtWidgets.QLineEdit(parent=self.tab_edit_product)
        self.line_edit_products_price_edit.setGeometry(QtCore.QRect(100, 100, 181, 20))
        self.line_edit_products_price_edit.setObjectName("line_edit_products_price_edit")
        self.label_product_category_edit = QtWidgets.QLabel(parent=self.tab_edit_product)
        self.label_product_category_edit.setGeometry(QtCore.QRect(20, 160, 71, 21))
        self.label_product_category_edit.setScaledContents(False)
        self.label_product_category_edit.setWordWrap(False)
        self.label_product_category_edit.setObjectName("label_product_category_edit")
        self.line_edit_products_category_edit = QtWidgets.QLineEdit(parent=self.tab_edit_product)
        self.line_edit_products_category_edit.setGeometry(QtCore.QRect(100, 160, 181, 20))
        self.line_edit_products_category_edit.setObjectName("line_edit_products_category_edit")
        self.line_edit_products_quantity_edit = QtWidgets.QLineEdit(parent=self.tab_edit_product)
        self.line_edit_products_quantity_edit.setGeometry(QtCore.QRect(100, 130, 181, 20))
        self.line_edit_products_quantity_edit.setObjectName("line_edit_products_quantity_edit")
        self.button_edit_products = QtWidgets.QPushButton(parent=self.tab_edit_product)
        self.button_edit_products.setGeometry(QtCore.QRect(20, 190, 261, 23))
        self.button_edit_products.setObjectName("button_edit_products")
        self.line_edit_products_name_edit = QtWidgets.QLineEdit(parent=self.tab_edit_product)
        self.line_edit_products_name_edit.setGeometry(QtCore.QRect(100, 70, 181, 20))
        self.line_edit_products_name_edit.setObjectName("line_edit_products_name_edit")
        self.line_edit_products_warehouse_id_edit = QtWidgets.QLineEdit(parent=self.tab_edit_product)
        self.line_edit_products_warehouse_id_edit.setGeometry(QtCore.QRect(100, 40, 181, 20))
        self.line_edit_products_warehouse_id_edit.setObjectName("line_edit_products_warehouse_id_edit")
        self.label_product_id_edit = QtWidgets.QLabel(parent=self.tab_edit_product)
        self.label_product_id_edit.setGeometry(QtCore.QRect(20, 10, 71, 20))
        self.label_product_id_edit.setObjectName("label_product_id_edit")
        self.line_edit_product_id = QtWidgets.QLineEdit(parent=self.tab_edit_product)
        self.line_edit_product_id.setGeometry(QtCore.QRect(100, 10, 181, 20))
        self.line_edit_product_id.setObjectName("line_edit_product_id")
        self.tab_products.addTab(self.tab_edit_product, "")
        self.tab_picture_product = QtWidgets.QWidget()
        self.tab_picture_product.setObjectName("tab_picture_product")
        self.labela_add_picture_id = QtWidgets.QLabel(parent=self.tab_picture_product)
        self.labela_add_picture_id.setGeometry(QtCore.QRect(20, 20, 251, 21))
        self.labela_add_picture_id.setObjectName("labela_add_picture_id")
        self.edit_add_picture_id = QtWidgets.QLineEdit(parent=self.tab_picture_product)
        self.edit_add_picture_id.setGeometry(QtCore.QRect(20, 50, 251, 20))
        self.edit_add_picture_id.setObjectName("edit_add_picture_id")
        self.button_select_picture = QtWidgets.QPushButton(parent=self.tab_picture_product)
        self.button_select_picture.setGeometry(QtCore.QRect(20, 80, 121, 23))
        self.button_select_picture.setObjectName("button_select_picture")
        self.button_save_picture = QtWidgets.QPushButton(parent=self.tab_picture_product)
        self.button_save_picture.setGeometry(QtCore.QRect(150, 80, 121, 23))
        self.button_save_picture.setObjectName("button_save_picture")
        self.label_file_name = QtWidgets.QLabel(parent=self.tab_picture_product)
        self.label_file_name.setGeometry(QtCore.QRect(20, 110, 111, 20))
        self.label_file_name.setObjectName("label_file_name")
        self.label_file_name_show = QtWidgets.QLabel(parent=self.tab_picture_product)
        self.label_file_name_show.setGeometry(QtCore.QRect(146, 110, 121, 20))
        self.label_file_name_show.setObjectName("label_file_name_show")
        self.label_show_picture_id = QtWidgets.QLabel(parent=self.tab_picture_product)
        self.label_show_picture_id.setGeometry(QtCore.QRect(20, 140, 251, 16))
        self.label_show_picture_id.setObjectName("label_show_picture_id")
        self.edit_show_picture_id = QtWidgets.QLineEdit(parent=self.tab_picture_product)
        self.edit_show_picture_id.setGeometry(QtCore.QRect(20, 170, 113, 20))
        self.edit_show_picture_id.setObjectName("edit_show_picture_id")
        self.button_show_picture = QtWidgets.QPushButton(parent=self.tab_picture_product)
        self.button_show_picture.setGeometry(QtCore.QRect(150, 170, 121, 23))
        self.button_show_picture.setObjectName("button_show_picture")
        self.tab_products.addTab(self.tab_picture_product, "")
        self.group_box_reports = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.group_box_reports.setGeometry(QtCore.QRect(30, 630, 171, 141))
        self.group_box_reports.setObjectName("group_box_reports")
        self.button_generate_reports = QtWidgets.QPushButton(parent=self.group_box_reports)
        self.button_generate_reports.setGeometry(QtCore.QRect(20, 60, 131, 23))
        self.button_generate_reports.setObjectName("button_generate_reports")
        self.button_show_reports = QtWidgets.QPushButton(parent=self.group_box_reports)
        self.button_show_reports.setGeometry(QtCore.QRect(20, 30, 131, 23))
        self.button_show_reports.setObjectName("button_show_reports")
        self.button_generate_reports_2 = QtWidgets.QPushButton(parent=self.group_box_reports)
        self.button_generate_reports_2.setGeometry(QtCore.QRect(20, 90, 131, 41))
        self.button_generate_reports_2.setObjectName("button_generate_reports_2")
        self.groupBox_ = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_.setGeometry(QtCore.QRect(330, 340, 311, 61))
        self.groupBox_.setObjectName("groupBox_")
        self.label_refresh = QtWidgets.QLabel(parent=self.groupBox_)
        self.label_refresh.setGeometry(QtCore.QRect(10, 20, 121, 16))
        self.label_refresh.setObjectName("label_refresh")
        self.label_refresh_time = QtWidgets.QLabel(parent=self.groupBox_)
        self.label_refresh_time.setGeometry(QtCore.QRect(140, 20, 151, 16))
        self.label_refresh_time.setText("")
        self.label_refresh_time.setObjectName("label_refresh_time")
        self.label_sum_product_price = QtWidgets.QLabel(parent=self.groupBox_)
        self.label_sum_product_price.setGeometry(QtCore.QRect(10, 40, 121, 16))
        self.label_sum_product_price.setObjectName("label_sum_product_price")
        self.label_sum_product_price_show = QtWidgets.QLabel(parent=self.groupBox_)
        self.label_sum_product_price_show.setGeometry(QtCore.QRect(140, 40, 151, 16))
        self.label_sum_product_price_show.setText("")
        self.label_sum_product_price_show.setObjectName("label_sum_product_price_show")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1304, 21))
        self.menubar.setDefaultUp(False)
        self.menubar.setObjectName("menubar")
        self.menuOther_actions = QtWidgets.QMenu(parent=self.menubar)
        self.menuOther_actions.setObjectName("menuOther_actions")
        self.menuReports = QtWidgets.QMenu(parent=self.menuOther_actions)
        self.menuReports.setObjectName("menuReports")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtGui.QAction(parent=MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAdd_picture_to_product = QtGui.QAction(parent=MainWindow)
        self.actionAdd_picture_to_product.setObjectName("actionAdd_picture_to_product")
        self.actionShow_Report = QtGui.QAction(parent=MainWindow)
        self.actionShow_Report.setCheckable(False)
        self.actionShow_Report.setObjectName("actionShow_Report")
        self.actionGenerate_reports = QtGui.QAction(parent=MainWindow)
        self.actionGenerate_reports.setObjectName("actionGenerate_reports")
        self.menuReports.addAction(self.actionShow_Report)
        self.menuReports.addAction(self.actionGenerate_reports)
        self.menuOther_actions.addAction(self.menuReports.menuAction())
        self.menubar.addAction(self.menuOther_actions.menuAction())

        self.retranslateUi(MainWindow)
        self.tab_warehouse.setCurrentIndex(0)
        self.tab_products.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.group_box_information.setTitle(_translate("MainWindow", "Information"))
        self.label_active_language_show.setText(_translate("MainWindow", "None"))
        self.label_active_user.setText(_translate("MainWindow", "Active user:"))
        self.label_active_user_show.setText(_translate("MainWindow", "None"))
        self.label_active_language.setText(_translate("MainWindow", "Language:"))
        self.label_date.setText(_translate("MainWindow", "Date:"))
        self.label_time_show.setText(_translate("MainWindow", "None"))
        self.label_date_show.setText(_translate("MainWindow", "None"))
        self.label_time.setText(_translate("MainWindow", "Time:"))
        self.group_box_selected_warehouse.setTitle(_translate("MainWindow", "Selected warehouse information"))
        self.label_warehouse_information_id.setText(_translate("MainWindow", "Warehouse id"))
        self.label_warehouse_information_id_show.setText(_translate("MainWindow", "None"))
        self.label_warehouse_information_name.setText(_translate("MainWindow", "Warehouse name"))
        self.label_warehouse_information_name_show.setText(_translate("MainWindow", "None"))
        self.label_warehouse_information_street_show.setText(_translate("MainWindow", "None"))
        self.label_warehouse_information_city_show.setText(_translate("MainWindow", "None"))
        self.label_warehouse_information_city.setText(_translate("MainWindow", "Warehouse city"))
        self.label_warehouse_information_street.setText(_translate("MainWindow", "Warehouse street"))
        self.label_warehouse_information_country_show.setText(_translate("MainWindow", "None"))
        self.label_warehouse_information_country.setText(_translate("MainWindow", "Warehouse country"))
        self.push_button_select_warehouse.setText(_translate("MainWindow", "Select warehouse"))
        self.button_show_products.setText(_translate("MainWindow", "Show Products"))
        self.button_show_warehouses.setText(_translate("MainWindow", "Show warehouses"))
        self.button_find_warehouse_by_product.setText(_translate("MainWindow", "Find"))
        self.group_delete_warehouse_product.setTitle(_translate("MainWindow", "Delete warehouse or product"))
        self.label_delete_warehouse.setText(_translate("MainWindow", "Delete by warehousue id"))
        self.label_delete_products.setText(_translate("MainWindow", "Delete by product id"))
        self.button_delete_warehouse.setText(_translate("MainWindow", "Delete warehouse"))
        self.button_delete_product.setText(_translate("MainWindow", "Delete product"))
        self.label_warehouse_city.setText(_translate("MainWindow", "Warehouse city"))
        self.label_warehouse_street.setText(_translate("MainWindow", "Warehouse street"))
        self.label_warehouse_name.setText(_translate("MainWindow", "Warehouse name"))
        self.button_save_warehouse.setText(_translate("MainWindow", "Save"))
        self.label_warehouse_country.setText(_translate("MainWindow", "Warehouse country"))
        self.tab_warehouse.setTabText(self.tab_warehouse.indexOf(self.tab_add_warehouse), _translate("MainWindow", "Add warehouse"))
        self.label_warehouse_city_edit.setText(_translate("MainWindow", "Warehouse city"))
        self.label_warehouse_street_edit.setText(_translate("MainWindow", "Warehouse street"))
        self.label_warehouse_name_edit.setText(_translate("MainWindow", "Warehouse name"))
        self.button_edit_warehouse.setText(_translate("MainWindow", "Edit"))
        self.label_warehouse_country_edit.setText(_translate("MainWindow", "Warehouse country"))
        self.label_warehouse_id_edit.setText(_translate("MainWindow", "Warehouse id"))
        self.tab_warehouse.setTabText(self.tab_warehouse.indexOf(self.tab_edit_warehouse), _translate("MainWindow", "Edit warehouse"))
        self.label_product_warehouse_id.setText(_translate("MainWindow", "Warehouse id"))
        self.label_product_name.setText(_translate("MainWindow", "Name"))
        self.label_product_quantity.setText(_translate("MainWindow", "Quantity"))
        self.button_save_product.setText(_translate("MainWindow", "Save"))
        self.label_product_category.setText(_translate("MainWindow", "Categorty"))
        self.label_product_price.setText(_translate("MainWindow", "Price"))
        self.tab_products.setTabText(self.tab_products.indexOf(self.tab_add_product), _translate("MainWindow", "Add product"))
        self.label_product_name_edit.setText(_translate("MainWindow", "Name"))
        self.label_product_price_edit.setText(_translate("MainWindow", "Price"))
        self.label_product_warehouse_id_edit.setText(_translate("MainWindow", "Warehouse id"))
        self.label_product_quantity_edit.setText(_translate("MainWindow", "Quantity"))
        self.label_product_category_edit.setText(_translate("MainWindow", "Categorty"))
        self.button_edit_products.setText(_translate("MainWindow", "Edit"))
        self.label_product_id_edit.setText(_translate("MainWindow", "Product id"))
        self.tab_products.setTabText(self.tab_products.indexOf(self.tab_edit_product), _translate("MainWindow", "Edit product"))
        self.labela_add_picture_id.setText(_translate("MainWindow", "Add product picture by product id"))
        self.button_select_picture.setText(_translate("MainWindow", "Select picture"))
        self.button_save_picture.setText(_translate("MainWindow", "Save to database"))
        self.label_file_name.setText(_translate("MainWindow", "File name:"))
        self.label_file_name_show.setText(_translate("MainWindow", "None"))
        self.label_show_picture_id.setText(_translate("MainWindow", "Enter product ID which picture you would like to see"))
        self.button_show_picture.setText(_translate("MainWindow", "Show picture"))
        self.tab_products.setTabText(self.tab_products.indexOf(self.tab_picture_product), _translate("MainWindow", "Add/Show product picture"))
        self.group_box_reports.setTitle(_translate("MainWindow", "Reports"))
        self.button_generate_reports.setText(_translate("MainWindow", "Generate reports"))
        self.button_show_reports.setText(_translate("MainWindow", "Show reports"))
        self.button_generate_reports_2.setText(_translate("MainWindow", "Generate reports"))
        self.groupBox_.setTitle(_translate("MainWindow", "Total cost of all products"))
        self.label_refresh.setText(_translate("MainWindow", "Time of the data refresh:"))
        self.label_sum_product_price.setText(_translate("MainWindow", "Sum of product price:"))
        self.menuOther_actions.setTitle(_translate("MainWindow", "Other actions"))
        self.menuReports.setTitle(_translate("MainWindow", "Reports"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionAdd_picture_to_product.setText(_translate("MainWindow", "Add picture to product"))
        self.actionShow_Report.setText(_translate("MainWindow", "Show Report"))
        self.actionGenerate_reports.setText(_translate("MainWindow", "Generate reports"))
