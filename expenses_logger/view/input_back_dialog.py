from expenses_logger.view.custom_widgets import CustomQDialog
from expenses_logger.view.ui.ui_input_back_dialog import Ui_InputBackDialog
from PySide2.QtWidgets import QWizard
from PySide2.QtCore import Qt


class InputBackDialog(CustomQDialog, Ui_InputBackDialog):
    is_last_response_yes = False

    def __init__(self, parent: QWizard) -> None:
        CustomQDialog.__init__(self, parent)
        self.setupUi(self)

        # connections
        self.pushButton_yes.clicked.connect(self.response_yes, Qt.UniqueConnection)
        self.pushButton_no.clicked.connect(self.response_no, Qt.UniqueConnection)

    def response_yes(self) -> None:
        InputBackDialog.is_last_response_yes = True
        self.close()

    def response_no(self) -> None:
        InputBackDialog.is_last_response_yes = False
        self.close()
