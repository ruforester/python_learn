import sys

from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QGridLayout, QLineEdit


class AgeCalculator(QWidget):
    def __init__(self):
        super().__init__()
        grid = QGridLayout()
        name_label = QLabel("Name:")
        name_line_edit = QLineEdit()
        date_birth_label = QLabel("Date of birth MM/DD/YYYY:")
        date_birth_line_edit = QLineEdit()

        grid.addWidget(name_label, 0, 0)
        grid.addWidget(name_line_edit, 0, 1)
        grid.addWidget(date_birth_label, 1, 0)
        grid.addWidget(date_birth_line_edit, 1, 1)

        self.setLayout(grid)


app = QApplication(sys.argv)
age_calculator = AgeCalculator()
age_calculator.show()
sys.exit(app.exec())
