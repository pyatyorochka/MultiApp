import os
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QTextEdit, QPushButton, QFileDialog, QMessageBox, QHBoxLayout
)

class NotepadWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()

        # Text editor
        self.text_edit = QTextEdit()
        self.layout.addWidget(self.text_edit)

        # Buttons for open/save
        btn_layout = QHBoxLayout()
        self.open_btn = QPushButton("Открыть")
        self.open_btn.clicked.connect(self.open_file)
        btn_layout.addWidget(self.open_btn)

        self.save_btn = QPushButton("Сохранить")
        self.save_btn.clicked.connect(self.save_file)
        btn_layout.addWidget(self.save_btn)

        self.layout.addLayout(btn_layout)
        self.setLayout(self.layout)

    def open_file(self):
        path, _ = QFileDialog.getOpenFileName(self, "Открыть файл", "", "Текстовые файлы (*.txt);;Все файлы (*.*)")
        if path:
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                self.text_edit.setPlainText(content)
            except Exception as e:
                QMessageBox.warning(self, "Ошибка", f"Не удалось открыть файл:\n{e}")

    def save_file(self):
        path, _ = QFileDialog.getSaveFileName(self, "Сохранить файл", "", "Текстовые файлы (*.txt);;Все файлы (*.*)")
        if path:
            try:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(self.text_edit.toPlainText())
                QMessageBox.information(self, "Сохранено", "Файл успешно сохранён.")
            except Exception as e:
                QMessageBox.warning(self, "Ошибка", f"Не удалось сохранить файл:\n{e}")
