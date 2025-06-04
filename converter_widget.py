from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, QMessageBox
)

class ConverterWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()

        type_layout = QHBoxLayout()
        type_layout.addWidget(QLabel("Тип конвертации:"))
        self.type_combo = QComboBox()
        # Добавим несколько примеров конвертаций
        self.type_combo.addItems([
            "°C → °F", "°F → °C",
            "м → футы", "футы → м",
            "кг → фунты", "фунты → кг"
        ])
        type_layout.addWidget(self.type_combo)
        self.layout.addLayout(type_layout)

        input_layout = QHBoxLayout()
        input_layout.addWidget(QLabel("Значение:"))
        self.input_val = QLineEdit()
        input_layout.addWidget(self.input_val)
        self.layout.addLayout(input_layout)

        self.convert_btn = QPushButton("Конвертировать")
        self.convert_btn.clicked.connect(self.convert)
        self.layout.addWidget(self.convert_btn)

        result_layout = QHBoxLayout()
        result_layout.addWidget(QLabel("Результат:"))
        self.result_val = QLineEdit()
        self.result_val.setReadOnly(True)
        result_layout.addWidget(self.result_val)
        self.layout.addLayout(result_layout)

        self.setLayout(self.layout)

    def convert(self):
        typ = self.type_combo.currentText()
        try:
            val = float(self.input_val.text())
        except ValueError:
            QMessageBox.warning(self, "Ошибка", "Введите корректное число.")
            return

        if typ == "°C → °F":
            res = val * 9/5 + 32
        elif typ == "°F → °C":
            res = (val - 32) * 5/9
        elif typ == "м → футы":
            res = val * 3.28084
        elif typ == "футы → м":
            res = val / 3.28084
        elif typ == "кг → фунты":
            res = val * 2.20462
        elif typ == "фунты → кг":
            res = val / 2.20462
        else:
            res = val
        self.result_val.setText(str(round(res, 4)))
