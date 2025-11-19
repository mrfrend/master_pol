from PyQt6.QtWidgets import QDialog, QMessageBox
from PyQt6.QtCore import pyqtSignal
from database.Database import db
from interface.select import Ui_Dialog
from windows.partner_history import PartnerHistory
from .editPartner import EditPartner
import pymysql
from dto.partner_card_info import PartnerCardInfo


class Admin(QDialog):
    deleted = pyqtSignal()
    edited = pyqtSignal(bool)

    def __init__(self, partner_info: PartnerCardInfo):
        super().__init__()
        self.ui = Ui_Dialog()
        self.partner_info = partner_info
        self.ui.setupUi(self)

        edit_button = self.ui.save_button
        delete_button = self.ui.save_button_2
        history_button = self.ui.save_button_3

        edit_button.clicked.connect(self.handle_save)
        delete_button.clicked.connect(self.handle_delete)
        history_button.clicked.connect(self.handle_history)

    def handle_save(self):
        self.EditPartner = EditPartner(self.partner_info)
        self.EditPartner.edited.connect(lambda: self.edited.emit(True))
        self.EditPartner.show()

    def handle_history(self):
        self.PartnerHistory = PartnerHistory(self.partner_info.id)
        self.PartnerHistory.show()
        self.close()

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
                self.deleted.emit()
                QMessageBox.information(self, "Успех", "Партнер удален")
            except pymysql.ProgrammingError as e:
                QMessageBox.warning(self, "Ошибка удаления партнера", str(e))
            self.close()
