◆簡易QRコード読取機能

・機能：
　　QRコード画像を読み取り、中身をデコードして表示する
　　デフォルトだとSJISで作成された内容をデコードする

・環境：
　　requirements.txtを参照

・準備
　　①仮想環境有効化
　　　　python -m venv myenv
　　　　Set-ExecutionPolicy RemoteSigned -Scope Process
　　　　.\myenv\Scripts\activate
　　②必要資材の導入
　　　　pip install -r requirements.txt

・使用方法：
　　①読み取りたいQRコード画像を以下のパスに上書きする
　　　　⇒INPUT\read.png
　　②exec.batを実行する

・補足
　　必要な環境は以下のコマンドでまとめている
　　pip freeze > requirements.txt
　　