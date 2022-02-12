import asyncio
import sys
from typing import List
from pathlib import Path
from datetime import datetime

from asyncqt import QEventLoop
from expenses_logger.globals import USERS, DATABASE_FILE, SYNC_NAS_DIR
from expenses_logger.logic.database import (
    empty_database,
    get_user_names,
    initialize_new_users,
)
from expenses_logger.logic.helper import sync_copy_database
from expenses_logger.view.create_new_database_dialog import CreateNewDatabaseDialog
from expenses_logger.view.non_ascii_names_dialog import NonAsciiNamesDialog
from expenses_logger.view.main_wizard import MainWizard
from PySide2.QtWidgets import QApplication


def valid_users_names(user_names: List[str]) -> bool:
    allowed_characters = "abcdefghijklmnopqrstuvwxyz0123456789- '"

    for user_name in user_names:
        lowered_user_name = user_name.strip().lower()
        tmp = all([ch in allowed_characters for ch in lowered_user_name])
        if not tmp:
            print("Invalid user_name in Config:", user_name)
            return False

    return True


def main() -> None:
    app = QApplication(sys.argv)
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)
    screenrect = app.primaryScreen().geometry()

    if not valid_users_names(USERS):
        dialog = NonAsciiNamesDialog()
        x = (screenrect.width() - dialog.width()) / 2
        y = (screenrect.height() - dialog.height()) / 2
        dialog.move(x, y)
        dialog.exec()
        exit()

    db_users = get_user_names()

    # user names changed? -> create new database
    if set(db_users) != set(USERS):
        dialog = CreateNewDatabaseDialog()
        x = (screenrect.width() - dialog.width()) / 2
        y = (screenrect.height() - dialog.height()) / 2
        dialog.move(x, y)
        dialog.exec()

        if CreateNewDatabaseDialog.is_last_response_yes:
            src_database = Path(__file__).parent.parent / DATABASE_FILE
            today = datetime.utcnow()
            target_database = (
                Path(SYNC_NAS_DIR)
                / f"{today.strftime('%Y.%m.%d_%H%Mutc')}__FINAL__{DATABASE_FILE}"
            )
            sync_copy_database(src_database, target_database)
            empty_database()
            initialize_new_users(USERS)
        else:
            exit()

    mainWindow = MainWizard(user_names=USERS, parent=None, desktop_size=None)
    mainWindow.move(screenrect.left(), screenrect.top())
    mainWindow.showFullScreen()
    mainWindow.activateWindow()

    with loop:
        sys.exit(loop.run_forever())


if __name__ == "__main__":
    main()
