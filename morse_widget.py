from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QTextEdit, QMessageBox, QLabel
)

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----','2': '..---','3': '...--','4': '....-',
    '5': '.....','6': '-....','7': '--...','8': '---..',
    '9': '----.','0': '-----', ', ':'--..--', '.':'.-.-.-',
    '?':'..--..','/':'-..-.','-':'-....-','(':'-.--.',
    ')':'-.--.-', ' ':'/'
}

class MorseWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()

        self.input = QLineEdit()
        self.input.setPlaceholderText("Введите текст для преобразования")
        self.layout.addWidget(self.input)

        btn_layout = QHBoxLayout()
        self.encode_btn = QPushButton("В Морзе")
        self.encode_btn.clicked.connect(self.encode_morse)
        btn_layout.addWidget(self.encode_btn)

        self.decode_btn = QPushButton("Из Морзе")
        self.decode_btn.clicked.connect(self.decode_morse)
        btn_layout.addWidget(self.decode_btn)

        self.layout.addLayout(btn_layout)

        self.output = QTextEdit()
        self.output.setReadOnly(True)
        self.layout.addWidget(self.output)

        self.setLayout(self.layout)

    def encode_morse(self):
        text = self.input.text().upper()
        if not text:
            QMessageBox.warning(self, "Ошибка", "Введите текст для кодирования.")
            return
        morse = ' '.join(MORSE_CODE_DICT.get(char, '') for char in text)
        self.output.setPlainText(morse)

    def decode_morse(self):
        code = self.input.text().strip()
        if not code:
            QMessageBox.warning(self, "Ошибка", "Введите последовательность Морзе для декодирования.")
            return
        inv_dict = {v: k for k, v in MORSE_CODE_DICT.items()}
        try:
            decoded = ''.join(inv_dict.get(sym, '') for sym in code.split())
            self.output.setPlainText(decoded)
        except Exception:
            self.output.setPlainText("Ошибка декодирования")
