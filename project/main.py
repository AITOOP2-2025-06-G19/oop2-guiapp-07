# main.py

import sys
from PySide6.QtWidgets import QApplication
from view import MainWindow
from controller import Controller

def main():
    app = QApplication(sys.argv)

    # Controller → View（循環参照にならないよう引数の順に注意）
    controller_placeholder = None
    view = MainWindow(controller_placeholder)
    controller = Controller(view)
    view.controller = controller  # Controllerを正式にセット
    view.connect_signals()

    view.connect_signals()

    view.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()