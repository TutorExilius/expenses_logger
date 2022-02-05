from functools import partial
from typing import List

from PySide6.QtWidgets import QWizard, QWizardPage, QListWidgetItem, QPushButton, QLabel

from expenses_logger.view.ui.ui_start_page import Ui_StartPage


class StartPage(QWizardPage, Ui_StartPage):
    # leave_start_page = pyqtSignal(str)

    def __init__(self, parent: QWizard, user_names: list[str]) -> None:
        QWizardPage.__init__(self)
        self.setupUi(self)

        self.users = ["Thomas", "Thompsen", "Ulf", "Ulli", "Tutor", "Wie-ihr-wollt"]
        self.refresh_user_list(self.users)

        # connections
        self.pushButton_clear.clicked.connect(self.line_edit_clear)

        for button_letter in self.frame_letters.children():
            if isinstance(button_letter, QPushButton):
                button_letter.clicked.connect(
                    partial(self.letter_button_clicked, button_letter.text())
                )

        self.lineEdit.mousePressEvent = self.set_cursor_to_end

        # partial(self.button_clicked, False, user_names[0]))
        # self.pushButton_name_2.clicked.connect(partial
        # (self.button_clicked, False, user_names[1]))

    def line_edit_clear(self) -> None:
        self.lineEdit.clear()
        self.refresh_user_list(self.users)

    def refresh_user_list(
        self, userlist: List[str], highlight_match: bool = False
    ) -> None:
        self.listWidget.clear()

        for user_name in sorted(userlist):
            label = QLabel(user_name)
            label.mousePressEvent = partial(self.name_clicked, user_name)

            item = QListWidgetItem()
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, label)

    def filter_userlist(self, matched_user_names: List[str]) -> None:
        self.listWidget.clear()

        for user_name in sorted(matched_user_names):
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

            label = QLabel(
                f"<font color=red>{matched_name_part.capitalize()}</font>"
                f"{remaining_name_part}"
            )
            label.mousePressEvent = partial(self.name_clicked, user_name)
            item = QListWidgetItem()
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, label)

    def name_clicked(self, user_name: object, *args: object, **kwargs: object) -> None:
        print("ich wurde geklickt", user_name)

    def show_filtered_user_list(self) -> None:
        self.listWidget.clear()

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
        self.lineEdit.insert(letter)
        self.show_filtered_user_list()

    def set_cursor_to_end(self, *args: object, **kwargs: object) -> None:
        self.lineEdit.setCursorPosition(len(self.lineEdit.text()))
