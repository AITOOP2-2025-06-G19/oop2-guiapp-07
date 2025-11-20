# main.py
import sys
from PySide6.QtWidgets import QApplication
from view import MainWindow
from controller import Controller

def main():
    app = QApplication(sys.argv)

    view = MainWindow()  # 最初は controller 渡さない
    controller = Controller(view)
    view.set_controller(controller)  # ← ここで connect する

    view.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()