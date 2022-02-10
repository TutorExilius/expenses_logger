"""
from functools import partial
from pathlib import Path

from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal, QCoreApplication
from PyQt5.QtWidgets import QListWidgetItem, QWizard, QWizardPage
from src.logic.helper import max_digits_behind_comma_arrived
from src.view.input_back_and_save_dialog import InputBackAndSaveDialog
from src.view.input_back_dialog import InputBackDialog
from src.view.remove_entries_dialog import RemoveEntriesDialog
"""
from functools import partial

from expenses_logger.logic.helper import (
    max_digits_behind_comma_arrived,
    remove_leading_zeros,
    cents_to_euro,
)
from expenses_logger.view.input_back_dialog import InputBackDialog
from expenses_logger.view.remove_entries_dialog import RemoveEntriesDialog
from expenses_logger.view.ui.ui_input_page import Ui_InputPage
from PySide2.QtCore import QCoreApplication, Qt, Signal, Slot
from PySide2.QtWidgets import QListWidgetItem, QWizard, QWizardPage


class InputPage(QWizardPage, Ui_InputPage):
    leave_input_page = Signal(str, str)

    def __init__(self, parent: QWizard) -> None:
        QWizardPage.__init__(self)
        self.setupUi(self)

        self.pushButton_remove_selected_items.setText("🗑")

        # connections
        self.pushButton_back.clicked.connect(
            self.back_button_clicked, Qt.UniqueConnection
        )
        self.pushButton_0.clicked.connect(
            partial(self.lineEdit_input_digit, False, "0")
        )
        self.pushButton_1.clicked.connect(
            partial(self.lineEdit_input_digit, False, "1")
        )
        self.pushButton_2.clicked.connect(
            partial(self.lineEdit_input_digit, False, "2")
        )
        self.pushButton_3.clicked.connect(
            partial(self.lineEdit_input_digit, False, "3")
        )
        self.pushButton_4.clicked.connect(
            partial(self.lineEdit_input_digit, False, "4")
        )
        self.pushButton_5.clicked.connect(
            partial(self.lineEdit_input_digit, False, "5")
        )
        self.pushButton_6.clicked.connect(
            partial(self.lineEdit_input_digit, False, "6")
        )
        self.pushButton_7.clicked.connect(
            partial(self.lineEdit_input_digit, False, "7")
        )
        self.pushButton_8.clicked.connect(
            partial(self.lineEdit_input_digit, False, "8")
        )
        self.pushButton_9.clicked.connect(
            partial(self.lineEdit_input_digit, False, "9")
        )
        self.pushButton_comma.clicked.connect(
            partial(self.lineEdit_input_digit, False, ",")
        )
        self.pushButton_del.clicked.connect(
            partial(self.lineEdit_input_digit, False, "DEL")
        )
        self.pushButton_add.clicked.connect(self.add_entry_to_list)
        self.pushButton_clear.clicked.connect(self.delete_input)
        self.pushButton_remove_selected_items.clicked.connect(
            self.remove_selected_items
        )
        self.listWidget_inputs.itemSelectionChanged.connect(
            self.entries_selection_changed
        )
        self.listWidget_inputs.model().rowsRemoved.connect(self.entries_changed)
        self.listWidget_inputs.model().rowsInserted.connect(self.entries_changed)

        """
        self.pushButton_save_back.clicked.connect(self.back_and_save_button_clicked)


       
        self.pushButton_0.clicked.connect(
            partial(self.lineEdit_input_digit, False, "0")
        )
        self.pushButton_1.clicked.connect(
            partial(self.lineEdit_input_digit, False, "1")
        )
        self.pushButton_2.clicked.connect(
            partial(self.lineEdit_input_digit, False, "2")
        )
        self.pushButton_3.clicked.connect(
            partial(self.lineEdit_input_digit, False, "3")
        )
        self.pushButton_4.clicked.connect(
            partial(self.lineEdit_input_digit, False, "4")
        )
        self.pushButton_5.clicked.connect(
            partial(self.lineEdit_input_digit, False, "5")
        )
        self.pushButton_6.clicked.connect(
            partial(self.lineEdit_input_digit, False, "6")
        )
        self.pushButton_7.clicked.connect(
            partial(self.lineEdit_input_digit, False, "7")
        )
        self.pushButton_8.clicked.connect(
            partial(self.lineEdit_input_digit, False, "8")
        )
        self.pushButton_9.clicked.connect(
            partial(self.lineEdit_input_digit, False, "9")
        )
        self.pushButton_comma.clicked.connect(
            partial(self.lineEdit_input_digit, False, ",")
        )
        self.pushButton_del.clicked.connect(
            partial(self.lineEdit_input_digit, False, "DEL")
        )
        self.pushButton_add.clicked.connect(self.add_entry_to_list)
        self.pushButton_clear.clicked.connect(self.delete_input)

   
    def delete_entries(self):
        self.listWidget_inputs.clear()
        self.label_total_amount.setText("0,00 €")
        self.pushButton_save_back.setEnabled(False)

   
 


    def back_and_save_button_clicked(self):
        dialog = InputBackAndSaveDialog(self)
        dialog.exec()

        if InputBackAndSaveDialog.is_last_response_yes:
            QCoreApplication.processEvents()

            name = self.label_name.text()
            self.leave_input_page.emit(name, self.label_total_amount.text())

   

    


"""

    @Slot(bool, str)
    def lineEdit_input_digit(self, _: bool, digit: str) -> None:
        old_text = self.lineEdit_input.text()
        if max_digits_behind_comma_arrived(old_text) and digit != "DEL":
            return

        if digit == "DEL":
            if not old_text:
                return

            deleting_digit = old_text[-1]

            if deleting_digit == ",":
                self.pushButton_comma.setEnabled(True)

            text = old_text[:-1]
        elif digit == ",":
            self.pushButton_comma.setEnabled(False)

            if old_text:
                text = old_text + digit
            else:
                text = "0" + digit
        else:
            text = old_text + digit

        self.lineEdit_input.setText(text)

        if text:
            self.pushButton_del.setEnabled(True)

            if max_digits_behind_comma_arrived(text):
                self.pushButton_add.setEnabled(True)
            else:
                self.pushButton_add.setEnabled(False)
        else:
            self.pushButton_del.setEnabled(False)
            self.pushButton_add.setEnabled(False)

    def entries_changed(self) -> None:
        if self.listWidget_inputs.count():
            self.pushButton_save_back.setEnabled(True)
        else:
            self.pushButton_save_back.setEnabled(False)

        total_amout_cents = 0

        for i in range(self.listWidget_inputs.count()):
            item = self.listWidget_inputs.item(i).text()
            item = item.replace(",", "")
            total_amout_cents += int(item)

        if total_amout_cents == 0:
            self.label_total_amount.setText("0,00 €")
        else:
            self.label_total_amount.setText(cents_to_euro(total_amout_cents))

    def entries_selection_changed(self) -> None:
        selected_items = self.listWidget_inputs.selectedItems()

        if selected_items:
            self.pushButton_remove_selected_items.setStyleSheet("font-weight: bold;")
            self.pushButton_remove_selected_items.setEnabled(True)
        else:
            self.pushButton_remove_selected_items.setStyleSheet("font-weight: normal;")
            self.pushButton_remove_selected_items.setEnabled(False)

    def remove_selected_items(self) -> None:
        dialog = RemoveEntriesDialog(self)
        dialog.exec()

        if RemoveEntriesDialog.is_last_response_yes:
            selected_items = self.listWidget_inputs.selectedItems()

            for item in selected_items:
                self.listWidget_inputs.takeItem(self.listWidget_inputs.row(item))
                del item

    def back_button_clicked(self) -> None:
        if self.listWidget_inputs.count() == 0:
            name = self.label_name.text()
            self.leave_input_page.emit(name, "")
            return

        dialog = InputBackDialog(self)
        dialog.exec()

        if InputBackDialog.is_last_response_yes:
            QCoreApplication.processEvents()

            name = self.label_name.text()
            self.leave_input_page.emit(name, "")

    def add_entry_to_list(self) -> None:
        text = remove_leading_zeros(self.lineEdit_input.text())
        item = QListWidgetItem(text)
        self.listWidget_inputs.addItem(item)
        self.delete_input()

    def delete_input(self) -> None:
        text = self.lineEdit_input.text()

        for _ in range(len(text)):
            self.lineEdit_input_digit(False, "DEL")

    def delete_entries(self) -> None:
        self.listWidget_inputs.clear()
        self.label_total_amount.setText("0,00 €")
        self.pushButton_save_back.setEnabled(False)
