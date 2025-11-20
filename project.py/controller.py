# controller.py

from model import ImageProcessor

class Controller:
    def __init__(self, view):
        self.view = view
        self.model = ImageProcessor()

    def handle_run_button_click(self):
        """View のボタンから呼ばれる処理"""
        self.view.update_status("画像処理中...")

        # Modelに実行指示
        output_path = self.model.process()

        if output_path is None:
            self.view.update_status("画像処理に失敗しました。")
            return

        # View に画像表示を依頼
        self.view.display_image(output_path)

        # ステータス更新
        self.view.update_status("処理完了！")