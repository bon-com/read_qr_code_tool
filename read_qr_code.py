import cv2
from pyzbar.pyzbar import decode

# 画像の読み込み
img = cv2.imread("INPUT\\read.png")

# QRコードの解析 ※結果はリストになる
decoded_objects = decode(img)

# QRコード１件だけを処理
if decoded_objects:
    obj = decoded_objects[0]
    raw_data = obj.data
    try:
        data = raw_data.decode("shift_jis")
    except UnicodeDecodeError:
        data = raw_data.decode("utf-8", errors="replace")
    print("読み取ったデータ:", data)
else:
    print("QRコードが見つかりませんでした。")


