import sys
import asyncio
from expenses_logger.globals import USERS

from asyncqt import QEventLoop
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import QSize

from expenses_logger.view.main_wizard import MainWizard


def main() -> None:
    app = QApplication(sys.argv)
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)

    mainWindow = MainWizard(user_names=USERS, parent=None, desktop_size=None)
    screenrect = app.primaryScreen().geometry()

    mainWindow.move(screenrect.left(), screenrect.top())
    mainWindow.setFixedSize(QSize(800, 480))
    mainWindow.show()

    with loop:
        sys.exit(loop.run_forever())


if __name__ == "__main__":
    main()
