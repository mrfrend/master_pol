from .select import Ui_Dialog
from PyQt6.QtWidgets import QDialog
from .editPartner import EditPartner

class Admin(QDialog):
    def __init__(self, partner_info):
        super().__init__()
        self.ui = Ui_Dialog()
        self.partner_info = partner_info
        self.ui.setupUi(self)
        self.ui.save_button.clicked.connect(self.on_clicked_edit)


    def on_clicked_edit(self):
        self.EditPartner = EditPartner(self.partner_info)
        self.EditPartner.show()




    
        