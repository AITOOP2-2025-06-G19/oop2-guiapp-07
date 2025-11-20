# view.py

from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QMainWindow
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.setWindowTitle("画像処理GUI")
        self.controller = controller

        # メインウィジェットとレイアウト
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # 実行ボタン
        self.run_button = QPushButton("画像処理を実行")
        # ボタンが押されたらControllerのメソッドを呼び出す
        self.run_button.clicked.connect(self.controller.handle_run_button_click)
        layout.addWidget(self.run_button)

        # 画像表示エリア
        self.image_label = QLabel("ここに処理後の画像が表示されます")
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setFixedSize(600, 400) # 表示サイズを固定
        layout.addWidget(self.image_label)

        # ステータス表示
        self.status_label = QLabel("待機中...")
        layout.addWidget(self.status_label)

    # Controllerから呼ばれて画像を表示するメソッド
    def display_image(self, image_path):
        pixmap = QPixmap(image_path)
        self.image_label.setPixmap(pixmap.scaled(self.image_label.size(), Qt.KeepAspectRatio))

    # Controllerから呼ばれてステータスを更新するメソッド
    def update_status(self, message):
        self.status_label.setText(message)