from PySide6.QtWidgets import QWizard, QWizardPage

from expenses_logger.view.ui.ui_start_page import Ui_StartPage


class StartPage(QWizardPage, Ui_StartPage):
    # leave_start_page = pyqtSignal(str)

    def __init__(self, parent: QWizard, user_names: list[str]) -> None:
        QWizardPage.__init__(self)
        self.setupUi(self)

        # connections
        # self.pushButton_name_1.clicked.connect(
        # partial(self.button_clicked, False, user_names[0]))
        # self.pushButton_name_2.clicked.connect(partial
        # (self.button_clicked, False, user_names[1]))

    def button_clicked(self, _: object, name: str) -> None:
        self.leave_start_page.emit(name)
