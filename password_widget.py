import random
import string
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QCheckBox, QSpinBox, QMessageBox
)
from PySide6.QtGui import QClipboard
from PySide6.QtCore import Qt

class PasswordWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()

        length_layout = QHBoxLayout()
        length_layout.addWidget(QLabel("Длина пароля:"))
        self.length_spin = QSpinBox()
        self.length_spin.setRange(6, 32)
        self.length_spin.setValue(12)
        length_layout.addWidget(self.length_spin)
        self.layout.addLayout(length_layout)

        self.upper_cb = QCheckBox("Заглавные буквы (A-Z)")
        self.upper_cb.setChecked(True)
        self.layout.addWidget(self.upper_cb)

        self.lower_cb = QCheckBox("Строчные буквы (a-z)")
        self.lower_cb.setChecked(True)
        self.layout.addWidget(self.lower_cb)

        self.digits_cb = QCheckBox("Цифры (0-9)")
        self.digits_cb.setChecked(True)
        self.layout.addWidget(self.digits_cb)

        self.symbols_cb = QCheckBox("Символы (!@#...)")
        self.symbols_cb.setChecked(True)
        self.layout.addWidget(self.symbols_cb)

        self.generate_btn = QPushButton("Сгенерировать пароль")
        self.generate_btn.clicked.connect(self.generate_password)
        self.layout.addWidget(self.generate_btn)

        out_layout = QHBoxLayout()
        self.password_out = QLineEdit()
        self.password_out.setReadOnly(True)
        out_layout.addWidget(self.password_out)
        self.copy_btn = QPushButton("Копировать")
        self.copy_btn.clicked.connect(self.copy_to_clipboard)
        out_layout.addWidget(self.copy_btn)
        self.layout.addLayout(out_layout)

        self.setLayout(self.layout)

    def generate_password(self):
        length = self.length_spin.value()
        pool = ""
        if self.upper_cb.isChecked():
            pool += string.ascii_uppercase
        if self.lower_cb.isChecked():
            pool += string.ascii_lowercase
        if self.digits_cb.isChecked():
            pool += string.digits
        if self.symbols_cb.isChecked():
            pool += string.punctuation

        if not pool:
            QMessageBox.warning(self, "Ошибка", "Выберите хотя бы один тип символов.")
            return

        pwd = "".join(random.choice(pool) for _ in range(length))
        self.password_out.setText(pwd)

    def copy_to_clipboard(self):
        clipboard = QApplication.clipboard()
        pwd = self.password_out.text()
        if pwd:
            clipboard.setText(pwd)
            QMessageBox.information(self, "Скопировано", "Пароль скопирован в буфер обмена.")
