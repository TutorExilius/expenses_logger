import sys
import asyncio
from expenses_logger.globals import USERS

from asyncqt import QEventLoop
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import QSize

from expenses_logger.view.main_wizard import MainWizard
from expenses_logger.view.create_new_database_dialog import CreateNewDatabaseDialog
from expenses_logger.logic.database import (
    get_user_names,
    empty_database,
    initialize_new_users,
)


def main() -> None:
    app = QApplication(sys.argv)
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)

    # DB creation / verification (USERS==db_users?)
    config_users = set(USERS)
    db_users = set(get_user_names())

    screenrect = app.primaryScreen().geometry()

    if config_users != db_users:
        dialog = CreateNewDatabaseDialog()
        x = (screenrect.width() - dialog.width()) / 2
        y = (screenrect.height() - dialog.height()) / 2
        dialog.move(x, y)
        dialog.exec()

        if CreateNewDatabaseDialog.is_last_response_yes:
            empty_database()
            initialize_new_users(USERS)
        else:
            exit()

        pass  # start dialog here. delete database and create new one with new users?
        # YES -> emptry_db + create_users + start app
        # No -> close app

    mainWindow = MainWizard(user_names=USERS, parent=None, desktop_size=None)
    mainWindow.move(screenrect.left(), screenrect.top())
    mainWindow.setFixedSize(QSize(800, 480))
    mainWindow.show()
    # mainWindow.showFullScreen()
    # mainWindow.activateWindow()

    with loop:
        sys.exit(loop.run_forever())


if __name__ == "__main__":
    main()
