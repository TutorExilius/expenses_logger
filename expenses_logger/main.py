import sys
from expenses_logger.globals import USERS

from asyncqt import QEventLoop
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import QSize

from expenses_logger.view.main_wizard import MainWizard


def main() -> None:
    app = QApplication(sys.argv)

    mainWindow = MainWizard(user_names=USERS, parent=None, desktop_size=None)

    mainWindow.show()

    app.exec()


if __name__ == "__main__":
    main()
