import random
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
)

class RandomWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()

        self.input = QLineEdit()
        self.input.setPlaceholderText("Введите варианты через запятую (например: да,нет,возможно)")
        self.layout.addWidget(self.input)

        self.choose_btn = QPushButton("Выбрать случайно")
        self.choose_btn.clicked.connect(self.choose_random)
        self.layout.addWidget(self.choose_btn)

        self.result_label = QLabel("")
        self.layout.addWidget(self.result_label)

        self.setLayout(self.layout)

    def choose_random(self):
        text = self.input.text().strip()
        if not text:
            QMessageBox.warning(self, "Ошибка", "Введите как минимум два варианта.")
            return
        options = [opt.strip() for opt in text.split(",") if opt.strip()]
        if len(options) < 2:
            QMessageBox.warning(self, "Ошибка", "Введите как минимум два варианта.")
            return
        choice = random.choice(options)
        self.result_label.setText(f"Результат: {choice}")
