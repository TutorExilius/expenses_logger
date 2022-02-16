from expenses_logger.view.custom_widgets import CustomQDialog
from expenses_logger.view.ui.ui_non_ascii_names_dialog import (
    Ui_NonAsciiNamesDialog,
)
from PySide2.QtWidgets import QWizard
from PySide2.QtCore import Qt


class NonAsciiNamesDialog(CustomQDialog, Ui_NonAsciiNamesDialog):
    is_last_response_yes = False

    def __init__(self, parent: QWizard = None) -> None:
        CustomQDialog.__init__(self, parent)
        self.setupUi(self)

        # connections
        self.pushButton_yes.clicked.connect(self.response_yes, Qt.UniqueConnection)
        self.pushButton_no.clicked.connect(self.response_no, Qt.UniqueConnection)

    def response_yes(self) -> None:
        NonAsciiNamesDialog.is_last_response_yes = True
        self.close()

    def response_no(self) -> None:
        NonAsciiNamesDialog.is_last_response_yes = False
        self.close()
