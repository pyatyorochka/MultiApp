import os
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLineEdit, QPushButton, QFileDialog, QMessageBox
)
from PySide6.QtGui import QDesktopServices
from PySide6.QtCore import QUrl
import qrcode

class QRWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()

        self.input = QLineEdit()
        self.input.setPlaceholderText("Введите текст или ссылку для QR-кода")
        self.layout.addWidget(self.input)

        self.filename_input = QLineEdit()
        self.filename_input.setPlaceholderText("Имя файла (например qr_code.png)")
        self.layout.addWidget(self.filename_input)

        self.generate_btn = QPushButton("Сгенерировать QR")
        self.generate_btn.clicked.connect(self.generate_qr)
        self.layout.addWidget(self.generate_btn)

        self.setLayout(self.layout)

    def generate_qr(self):
        data = self.input.text().strip()
        if not data:
            QMessageBox.warning(self, "Внимание", "Пожалуйста, введите данные для QR-кода.")
            return

        filename = self.filename_input.text().strip()
        if not filename:
            filename = "qr_code.png"
        elif not any(filename.lower().endswith(ext) for ext in (".png", ".jpg", ".jpeg", ".bmp", ".gif")):
            filename += ".png"

        save_dir = os.path.expanduser(os.path.join("~", "QR_Results"))
        os.makedirs(save_dir, exist_ok=True)
        full_path = os.path.join(save_dir, filename)

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(full_path)

        msg = QMessageBox(self)
        msg.setWindowTitle("Готово")
        msg.setText(f"QR-код сохранён:\n{full_path}")
        open_btn = msg.addButton("Открыть папку", QMessageBox.ActionRole)
        msg.addButton("ОК", QMessageBox.AcceptRole)
        msg.exec_()

        if msg.clickedButton() == open_btn:
            folder_url = QUrl.fromLocalFile(os.path.dirname(full_path))
            QDesktopServices.openUrl(folder_url)
