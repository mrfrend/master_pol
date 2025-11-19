from interface.partner_history import Ui_Form
from PyQt6.QtWidgets import QWidget, QTableWidgetItem, QHeaderView
from database.Database import db


class PartnerHistory(QWidget, Ui_Form):
    def __init__(self, partner_id: int):
        super().__init__()
        self.partner_id = partner_id
        self.setupUi(self)
        self.load_history()
        self.back_button.clicked.connect(self.handle_back)

    def handle_back(self):
        from .AdminChoice import Admin

        self.Admin = Admin(db.get_partner_info(self.partner_id))
        self.Admin.show()
        self.close()

    def load_history(self):
        history_rows = db.get_partner_history(self.partner_id)
        self.tableWidget.setRowCount(len(history_rows))
        self.tableWidget.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )
        for i, row in enumerate(history_rows):
            self.tableWidget.setItem(i, 0, QTableWidgetItem(row["product_name"]))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(row["quantity"])))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(str(row["sale_date"])))
