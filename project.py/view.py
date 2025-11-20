# view.py

from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QMainWindow
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self, controller=None):
        super().__init__()
        self.setWindowTitle("画像処理GUI")
        self.controller = controller

        # メインウィジェットとレイアウト
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # 実行ボタン
        self.run_button = QPushButton("画像処理を実行")
        layout.addWidget(self.run_button)

        # 画像表示エリア
        self.image_label = QLabel("ここに処理後の画像が表示されます")
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setFixedSize(600, 400)
        layout.addWidget(self.image_label)

        # ステータス表示
        self.status_label = QLabel("待機中...")
        layout.addWidget(self.status_label)

    # ← Controller が後から渡されるのでそこで connect する
    def set_controller(self, controller):
        self.controller = controller
        self.run_button.clicked.connect(self.controller.handle_run_button_click)

    # Controller から呼ばれる
    def display_image(self, image_path):
        pixmap = QPixmap(image_path)
        self.image_label.setPixmap(
            pixmap.scaled(self.image_label.size(), Qt.KeepAspectRatio)
        )

    def update_status(self, message):
        self.status_label.setText(message)
    