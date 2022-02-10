from expenses_logger.view.ui.ui_create_new_database_dialog import (
    Ui_CreateNewDatabaseDialog,
)
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QDialog, QWizard


class CreateNewDatabaseDialog(QDialog, Ui_CreateNewDatabaseDialog):
    is_last_response_yes = False

    def __init__(self, parent: QWizard = None) -> None:
        QDialog.__init__(self, parent)
        self.setupUi(self)

        self.setWindowFlag(Qt.WindowMinimizeButtonHint, False)
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.setWindowFlag(Qt.WindowMinMaxButtonsHint, False)
        self.setWindowFlag(Qt.FramelessWindowHint, True)

        # connections
        self.pushButton_yes.clicked.connect(self.response_yes, Qt.UniqueConnection)
        self.pushButton_no.clicked.connect(self.response_no, Qt.UniqueConnection)

    def response_yes(self) -> None:
        CreateNewDatabaseDialog.is_last_response_yes = True
        self.close()

    def response_no(self) -> None:
        CreateNewDatabaseDialog.is_last_response_yes = False
        self.close()
