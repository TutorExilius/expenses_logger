from functools import partial
from typing import Dict, List

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

    def filter_userlist(self, matched_user_names: Dict[str, str]) -> None:
        self.listWidget.clear()

        for user_name in sorted(matched_user_names.keys()):
            matched_letters = [letter for letter in self.lineEdit.text()]
            _matched_letters = []

            for letter in user_name:
                if not letter.isalpha():
                    _matched_letters.append(letter)
                    continue

                if not matched_letters:
                    break

                matched_letters.pop()
                _matched_letters.append(letter)

            matched_letters_str = "".join(_matched_letters)
            label_text = user_name[len(matched_letters_str) :]
            matched_letters_str = (
                f"<font color=red>{matched_letters_str.capitalize()}</font>"
            )

            label = QLabel(f"{matched_letters_str}{label_text}")
            label.mousePressEvent = partial(self.name_clicked, user_name)
            item = QListWidgetItem()
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, label)

    def name_clicked(self, user_name: object, *args: object, **kwargs: object) -> None:
        print("ich wurde geklickt", user_name)

    def show_filtered_user_list(self) -> None:
        self.listWidget.clear()

        alpha_only_users_map = {}

        for user_name in self.users:
            alpha_only_username = "".join(
                [letter for letter in user_name if letter.isalpha()]
            )

            if alpha_only_username.lower().startswith(self.lineEdit.text().lower()):
                alpha_only_users_map[user_name] = alpha_only_username

        self.filter_userlist(alpha_only_users_map)

    def letter_button_clicked(self, letter: str) -> None:
        self.lineEdit.insert(letter)
        self.show_filtered_user_list()

    def set_cursor_to_end(self, *args: object, **kwargs: object) -> None:
        self.lineEdit.setCursorPosition(len(self.lineEdit.text()))
