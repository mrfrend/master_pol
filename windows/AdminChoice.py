from PyQt6.QtWidgets import QDialog, QMessageBox
from PyQt6.QtCore import pyqtSignal
from database.Database import db
from interface.select import Ui_Dialog
from .editPartner import EditPartner
import pymysql
from dto.partner_card_info import PartnerCardInfo


class Admin(QDialog):
    deleted = pyqtSignal(PartnerCardInfo)

    def __init__(self, partner_info: PartnerCardInfo):
        super().__init__()
        self.ui = Ui_Dialog()
        self.partner_info = partner_info
        self.ui.setupUi(self)

        edit_button = self.ui.save_button
        delete_button = self.ui.save_button_2

        edit_button.clicked.connect(self.handle_save)
        delete_button.clicked.connect(self.handle_delete)

    def handle_save(self):
        self.EditPartner = EditPartner(self.partner_info)
        self.EditPartner.show()

    def handle_delete(self):
        reply = QMessageBox.question(
            self,
            "Удаление",
            "Вы уверены, что хотите удалить этого партнера?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No,
        )

        if reply == QMessageBox.StandardButton.Yes:
            try:
                db.delete_partner(self.partner_info.id)
                self.deleted.emit(self.partner_info)
                QMessageBox.information(self, "Успех", "Партнер удален")
            except pymysql.ProgrammingError as e:
                QMessageBox.warning(self, "Ошибка удаления партнера", str(e))
            self.close()
