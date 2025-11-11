from interface.AddPartner import Ui_MainWindow
from PyQt6 import QtWidgets, QtCore
from database.Database import db
from dto.partner_card_info import PartnerAddDTO
import pymysql


class AddPartner(QtWidgets.QMainWindow):
    inserted = QtCore.pyqtSignal()

    def __init__(self, partner_info):
        super().__init__()
        self.partner_info = partner_info
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.load_partner_types()
        self.ui.save_button.clicked.connect(self.handle_save)
        self.ui.cancel_button.clicked.connect(self.close)

    def load_partner_types(self):
        types = db.get_partners_types()
        for t in types:
            self.ui.typeBox.addItem(t["name"], t["id"])

    def handle_save(self):
        type_partner_id = self.ui.typeBox.currentData() + 1
        partner_name = self.ui.partner_name_edit.text()
        first_name = self.ui.first_name_edit.text()
        last_name = self.ui.last_name_edit.text()
        middle_name = self.ui.middle_name_edit.text()
        email = self.ui.email_edit.text()
        phone = self.ui.phone_edit.text()
        address = self.ui.address_edit.text()
        INN = self.ui.INN_edit.text()
        rating = self.ui.rating_spinbox.value()

        try:
            if not all(
                [partner_name, first_name, last_name, email, phone, address, INN]
            ):
                raise ValueError("Заполните все поля")

            partner_info = PartnerAddDTO(
                type_id=type_partner_id,
                partner_name=partner_name,
                first_name=first_name,
                last_name=last_name,
                middle_name=middle_name,
                email=email,
                phone_partner=phone,
                address=address,
                inn_number=INN,
                rating=rating,
            )
            db.insert_partner(partner_info)

            self.inserted.emit()
            QtWidgets.QMessageBox.information(self, "Успех", "Партнер добавлен")
            self.close()
        except (ValueError, pymysql.ProgrammingError) as e:
            QtWidgets.QMessageBox.warning(self, "Ошибка", str(e))
            return


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
