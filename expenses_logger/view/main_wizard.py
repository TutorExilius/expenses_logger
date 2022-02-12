from datetime import datetime
from enum import auto, Enum
from pathlib import Path
from typing import List

from expenses_logger import globals
from expenses_logger.logic.database import (
    add_amount,
)
from expenses_logger.logic.helper import copy_database, print_log
from expenses_logger.view.input_page import InputPage
from expenses_logger.view.start_page import StartPage
from PySide2.QtCore import QSize, Qt, Slot
from PySide2.QtWidgets import QWidget, QWizard


class PageNumber(Enum):
    START_PAGE = auto()
    INPUT_PAGE = auto()


class MainWizard(QWizard):
    def __init__(
        self,
        user_names: List[str],
        parent: QWidget = None,
        desktop_size: QSize = None,
    ) -> None:
        if not user_names:
            raise ValueError("User list is empty.")

        super().__init__(parent)

        self.setWizardStyle(QWizard.NStyles)
        self.setButtonLayout([])

        self.user_names = user_names

        self._pages = {}
        self._pages[PageNumber.START_PAGE] = self.addPage(StartPage(self, user_names))
        self._pages[PageNumber.INPUT_PAGE] = self.addPage(InputPage(self))

        self.update_year_label(datetime.utcnow().year)

        # self.setModal(False)

        self.setWindowFlag(Qt.FramelessWindowHint, True)
        self.setWindowFlag(Qt.WindowStaysOnTopHint, True)
        self.setWindowState(self.windowState() | Qt.WindowFullScreen)

        # connections
        self.page(self._pages[PageNumber.START_PAGE]).leave_start_page.connect(
            self.leave_start_page, Qt.UniqueConnection
        )
        self.page(self._pages[PageNumber.INPUT_PAGE]).leave_input_page.connect(
            self.leave_input_page, Qt.UniqueConnection
        )

    def update_year_label(self, year: int) -> None:
        start_page = self.page(self._pages[PageNumber.START_PAGE])
        start_page.label_year.setText(str(year))

    @Slot(str)
    def leave_start_page(self, user_name: str) -> None:
        self._reset_start_page()

        print_log(
            page_name="StartPage",
            username=user_name,
            action="is entering the InputPage",
        )

        self._next(user_name)

    @Slot(str, str)
    def leave_input_page(self, user_name: str, amount: str) -> None:
        self._reset_input_page()

        if amount:
            print_log(
                page_name="InputPage",
                username=user_name,
                action=f"is leaving the InputPage. Save {amount}",
            )
            self._back_and_save(user_name, amount)
        else:
            print_log(
                page_name="InputPage",
                username=user_name,
                action="is leaving the InputPage without saving",
            )
            self._back(user_name)

    def _next(self, user_name: str) -> None:
        input_page = self.page(self._pages[PageNumber.INPUT_PAGE])
        input_page.label_name.setText(user_name)
        input_page.label_name.setStyleSheet("text-decoration: underline;")

        super().next()

    def _back_and_save(self, user_name: str, amount: str) -> None:
        amount = amount.replace("€", "").strip()
        amount_in_cent: int = int(
            amount.replace(",", "")
        )  # remove comma to interpret as cent

        if amount_in_cent > 0:
            add_amount(
                user_name=user_name,
                amount_in_cents=amount_in_cent,
            )

            src_database = Path(__file__).parent.parent.parent / globals.DATABASE_FILE
            target_database = Path(globals.SYNC_NAS_DIR) / globals.DATABASE_FILE
            copy_database(src_database, target_database)

            start_page = self.page(self._pages[PageNumber.START_PAGE])
            start_page.reload_user_amounts()
            start_page.update_ui()

        super().back()

    def _back(self, user_name: str) -> None:
        start_page = self.page(self._pages[PageNumber.START_PAGE])
        start_page.listWidget.clearSelection()

        super().back()

    def _reset_input_page(self) -> None:
        input_page = self.page(self._pages[PageNumber.INPUT_PAGE])
        input_page.delete_input()
        input_page.delete_entries()

    def _reset_start_page(self) -> None:
        start_page = self.page(self._pages[PageNumber.START_PAGE])
        start_page.line_edit_clear()
