from expenses_logger.view.ui.ui_remove_entries_dialog import Ui_RemoveEntriesDialog
from PySide2.QtWidgets import QDialog, QWizard
from PySide2.QtCore import Qt


class RemoveEntriesDialog(QDialog, Ui_RemoveEntriesDialog):
    is_last_response_yes = False

    def __init__(self, parent: QWizard) -> None:
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
        RemoveEntriesDialog.is_last_response_yes = True
        self.close()

    def response_no(self) -> None:
        RemoveEntriesDialog.is_last_response_yes = False
        self.close()