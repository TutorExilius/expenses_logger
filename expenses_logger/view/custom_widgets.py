from expenses_logger.logic.helper import cents_to_euro
from PySide2.QtWidgets import QHBoxLayout, QLabel, QSizePolicy, QSpacerItem, QWidget


class ListItem(QWidget):
    def __init__(self, user_name: str, amount_in_cent: int) -> None:
        super().__init__()
        self.init_ui(user_name, amount_in_cent)

    def init_ui(self, user_name: str, amount_in_cent: int) -> None:
        h_layout = QHBoxLayout()
        h_layout.setSpacing(0)
        h_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(h_layout)

        user_name_label = QLabel(user_name)

        """
        does not work yet :(
        
        try:
            import locale
        
            locale.setlocale(locale.LC_ALL, "")
            print("Yepp")
        except Exception as e:
            logging.exception(e)
        
        print(locale.getlocale())
        
        amount_str = f"{amount_in_cent / 100:.2f} €"
        """

        amount_str = cents_to_euro(amount_in_cent)
        amount_str_label = QLabel(amount_str)

        h_layout.addWidget(user_name_label)
        h_layout.addItem(
            QSpacerItem(
                20, 0, QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding
            )
        )
        h_layout.addWidget(amount_str_label)
