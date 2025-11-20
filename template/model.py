# model.py

import cv2
import numpy as np
from my_module.K24027.lecture05_camera_image_capture import MyVideoCapture

class ImageProcessor:

    def process(self) -> str | None:
        """白色部分をカメラ画像で置換して保存する"""

        # カメラキャプチャ
        cap = MyVideoCapture()
        cap.run()
        capture_img = cap.get_img()

        if capture_img is None:
            print("カメラ画像が取得できませんでした")
            return None

        # Google画像読み込み
        google_img = cv2.imread('/Users/k24027kk/work/oop2/05/issue/images/google.png')
        if google_img is None:
            print("google画像が読み込めません")
            return None

        g_h, g_w, _ = google_img.shape
        c_h, c_w, _ = capture_img.shape

        output = google_img.copy()

        # 白色を置換
        for y in range(g_h):
            for x in range(g_w):
                b, g, r = google_img[y, x]
                if (b, g, r) == (255, 255, 255):
                    cx = x % c_w
                    cy = y % c_h
                    output[y, x] = capture_img[cy, cx]

        output_path = "lecture05_output.png"
        cv2.imwrite(output_path, output)

        return output_path