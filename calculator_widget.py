from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLineEdit, QGridLayout, QPushButton, QSizePolicy
)
from PySide6.QtCore import Qt

class CalculatorWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.display.setFixedHeight(40)
        self.layout.addWidget(self.display)

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+'],
            ['C', '(', ')', '<-']
        ]

        grid = QGridLayout()
        for row_idx, row in enumerate(buttons):
            for col_idx, btn_text in enumerate(row):
                btn = QPushButton(btn_text)
                btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                btn.clicked.connect(self.on_button_clicked)
                grid.addWidget(btn, row_idx, col_idx)

        self.layout.addLayout(grid)
        self.setLayout(self.layout)

    def on_button_clicked(self):
        btn = self.sender()
        text = btn.text()

        if text == 'C':
            self.display.clear()
        elif text == '<-':
            current = self.display.text()
            self.display.setText(current[:-1])
        elif text == '=':
            expr = self.display.text()
            try:
                result = str(eval(expr))
                self.display.setText(result)
            except Exception:
                self.display.setText("Ошибка")
        else:
            self.display.setText(self.display.text() + text)
