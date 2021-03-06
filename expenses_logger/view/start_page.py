from functools import partial
from typing import List

from expenses_logger.logic.database import get_user_amounts
from expenses_logger.view.custom_widgets import ListItem
from expenses_logger.view.ui.ui_start_page import Ui_StartPage
from PySide2.QtCore import QEvent, Qt, Signal
from PySide2.QtWidgets import (
    QListWidgetItem,
    QPushButton,
    QWizard,
    QWizardPage,
)


class StartPage(QWizardPage, Ui_StartPage):
    leave_start_page = Signal(str)

    def __init__(self, parent: QWizard, user_names: list[str]) -> None:
        QWizardPage.__init__(self)
        self.setupUi(self)

        self.users = sorted(user_names, key=lambda name: name.casefold())
        self.user_amount_map = get_user_amounts()

        self.refresh_user_list()

        # connections
        self.pushButton_clear.clicked.connect(self.line_edit_clear, Qt.UniqueConnection)
        self.listWidget.itemSelectionChanged.connect(
            self.selection_name_clicked, Qt.UniqueConnection
        )

        for button_letter in self.frame_letters.children():
            if isinstance(button_letter, QPushButton):
                button_letter.clicked.connect(
                    partial(self.letter_button_clicked, button_letter.text()),
                    Qt.UniqueConnection,
                )

        self.lineEdit.mousePressEvent = self.set_cursor_to_end

    def reload_user_amounts(self) -> None:
        self.user_amount_map = get_user_amounts()

    def line_edit_clear(self) -> None:
        self.lineEdit.clear()
        self.pushButton_clear.setEnabled(False)
        self.refresh_user_list()

    def update_ui(self) -> None:
        self.refresh_user_list()

    def refresh_user_list(self) -> None:
        self._clear_list_widget()

        for user_name in self.users:
            amount_in_cent = self.user_amount_map[user_name]
            self.add_item_in_list_widget(
                title=user_name, user_name=user_name, amount_in_cent=amount_in_cent
            )

        if len(self.users) <= 1:
            self.frame_letters.setEnabled(False)
        else:
            self.frame_letters.setEnabled(True)

    def filter_userlist(self, matched_user_names: List[str]) -> None:
        self._clear_list_widget()

        if len(matched_user_names) <= 1:
            self.frame_letters.setEnabled(False)

        for user_name in matched_user_names:
            matched_letters = []
            pattern_letters = [letter for letter in self.lineEdit.text()]

            for letter in user_name:
                if not pattern_letters:
                    break

                if not letter.isalpha():
                    matched_letters.append(letter)
                    continue

                matched_letters.append(letter)
                pattern_letters.pop()

            matched_name_part = "".join(matched_letters)
            remaining_name_part = user_name[len(matched_name_part) :]

            self.add_item_in_list_widget(
                title=f"<font color=red>{matched_name_part}</font>"
                f"{remaining_name_part}",
                user_name=user_name,
                amount_in_cent=self.user_amount_map[user_name],
            )

    def add_item_in_list_widget(
        self, title: str, user_name: str, amount_in_cent: int
    ) -> None:
        item_widget = ListItem(title, amount_in_cent)
        item_widget._origin_user_name = user_name

        item = QListWidgetItem()

        self.listWidget.addItem(item)
        self.listWidget.setItemWidget(item, item_widget)

    def selection_name_clicked(self) -> None:
        if not self.listWidget.selectedItems():
            return

        item = self.listWidget.selectedItems()[0]
        user_name = self.listWidget.itemWidget(item)._origin_user_name

        self.leave_start_page.emit(user_name)

    def show_filtered_user_list(self) -> None:
        self._clear_list_widget()

        pattern = self.lineEdit.text().lower()
        matched_user_names = []

        for user_name in self.users:
            alpha_only_username = "".join(
                [letter for letter in user_name if letter.isalpha()]
            ).lower()

            if alpha_only_username.startswith(pattern):
                matched_user_names.append(user_name)

        self.filter_userlist(matched_user_names)

    def letter_button_clicked(self, letter: str) -> None:
        self.pushButton_clear.setEnabled(True)
        self.lineEdit.insert(letter)
        self.show_filtered_user_list()

    def set_cursor_to_end(self, event: QEvent) -> None:
        self.lineEdit.setCursorPosition(len(self.lineEdit.text()))
        event.accept()

    def _clear_list_widget(self) -> None:
        self.blockSignals(True)
        self.listWidget.clearSelection()
        self.listWidget.clear()
        self.blockSignals(False)
