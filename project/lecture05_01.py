import numpy as np
import cv2
from my_module.K24027.lecture05_camera_image_capture import MyVideoCapture

def lecture05_01():
    # カメラキャプチャ実行
    app = MyVideoCapture()
    capture_img: cv2.Mat = app.run()  # run()でキャプチャ画像を返す想定
    capture_img = app.get_img()

    # 画像を読み込み
    google_img = cv2.imread('template/images/google.png')

    if google_img is None:
        print("google.png が読み込めませんでした。")
        return -1
    if capture_img is None or capture_img.size == 0:
        print("カメラ画像が取得できませんでした。")
        return -1

    g_height, g_width, g_channel = google_img.shape
    c_height, c_width, c_channel = capture_img.shape

    print("google画像サイズ:", google_img.shape)
    print("カメラ画像サイズ:", capture_img.shape)

    # 白色部分をカメラ画像で置換
    output_img = google_img.copy()
    for y in range(g_height):
        for x in range(g_width):
            b, g, r = google_img[y, x]
            # 白(255,255,255)なら置換
            if (b, g, r) == (255, 255, 255):
                # カメラ画像上の対応する座標（タイル状に並べる）
                cx = x % c_width
                cy = y % c_height
                output_img[y, x] = capture_img[cy, cx]

    # 画像を保存
    cv2.imwrite('lecture05_01_K24027.png', output_img)
    print("lecture05_01_K24027.png を保存しました。")
    result = cv2.imwrite('lecture05_01_K24027.png', output_img)

if __name__ == "__main__":
    lecture05_01()