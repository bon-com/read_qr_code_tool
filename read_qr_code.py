import cv2
from pyzbar.pyzbar import decode

# 画像の読み込み
img = cv2.imread("INPUT\\read.png")

# QRコードの解析
decoded_objects = decode(img)

# 各QRコードを処理
for obj in decoded_objects:
    raw_data = obj.data
    try:
        data = raw_data.decode("shift_jis")
    except UnicodeDecodeError:
        data = raw_data.decode("utf-8", errors="replace")
    print("読み取ったデータ:", data)

input("\nEnterキーを押すと終了します")