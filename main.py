import sys
import os
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout
)
import qdarkstyle

from qr_widget import QRWidget
from password_widget import PasswordWidget
from calculator_widget import CalculatorWidget
from notepad_widget import NotepadWidget
from converter_widget import ConverterWidget
from random_widget import RandomWidget
from morse_widget import MorseWidget
from timer_widget import TimerWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Многофункциональное приложение")
        self.setMinimumSize(800, 600)

        tabs = QTabWidget()
        tabs.addTab(QRWidget(), "QR-Код")
        tabs.addTab(PasswordWidget(), "Пароли")
        tabs.addTab(CalculatorWidget(), "Калькулятор")
        tabs.addTab(NotepadWidget(), "Блокнот")
        tabs.addTab(ConverterWidget(), "Конвертер")
        tabs.addTab(RandomWidget(), "Случайный выбор")
        tabs.addTab(MorseWidget(), "Морзе")
        tabs.addTab(TimerWidget(), "Таймер")

        self.setCentralWidget(tabs)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Apply dark theme explicitly for PySide6 (без попыток искать PyQt6)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())

    window = MainWindow()
    window.show()
    sys.exit(app.exec())
