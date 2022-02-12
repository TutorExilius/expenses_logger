from expenses_logger.view.ui.ui_non_ascii_names_dialog import (
    Ui_NonAsciiNamesDialog,
)
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QDialog, QWizard


class NonAsciiNamesDialog(QDialog, Ui_NonAsciiNamesDialog):
    def __init__(self, parent: QWizard = None) -> None:
        QDialog.__init__(self, parent)
        self.setupUi(self)

        self.setWindowFlag(Qt.WindowMinimizeButtonHint, False)
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.setWindowFlag(Qt.WindowMinMaxButtonsHint, False)
        self.setWindowFlag(Qt.FramelessWindowHint, True)

        # connections
        self.pushButton_ok.clicked.connect(self.close, Qt.UniqueConnection)
