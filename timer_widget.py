from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
)
from PySide6.QtCore import QTimer, QTime, Qt

class TimerWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()

        self.time_label = QLabel("00:00:00")
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("font-size: 24px;")
        self.layout.addWidget(self.time_label)

        btn_layout = QHBoxLayout()
        self.start_btn = QPushButton("Старт")
        self.start_btn.clicked.connect(self.start_timer)
        btn_layout.addWidget(self.start_btn)

        self.stop_btn = QPushButton("Стоп")
        self.stop_btn.clicked.connect(self.stop_timer)
        btn_layout.addWidget(self.stop_btn)

        self.reset_btn = QPushButton("Сброс")
        self.reset_btn.clicked.connect(self.reset_timer)
        btn_layout.addWidget(self.reset_btn)

        self.layout.addLayout(btn_layout)
        self.setLayout(self.layout)

        self.timer = QTimer()
        self.timer.setInterval(1000)  # 1 сек
        self.timer.timeout.connect(self.update_time)
        self.elapsed = 0  # секунд

    def start_timer(self):
        if not self.timer.isActive():
            self.timer.start()

    def stop_timer(self):
        if self.timer.isActive():
            self.timer.stop()

    def reset_timer(self):
        self.timer.stop()
        self.elapsed = 0
        self.time_label.setText("00:00:00")

    def update_time(self):
        self.elapsed += 1
        hours = self.elapsed // 3600
        minutes = (self.elapsed % 3600) // 60
        seconds = self.elapsed % 60
        self.time_label.setText(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
