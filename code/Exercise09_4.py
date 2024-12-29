"""Exercise09_4.py"""
try:
    # キーボードからファイル名を入力する
    fname = input("ファイル名を入力してください：")

    # ファイルを開く
    f = open(fname, "r", encoding="utf-8")

except Exception as e:
    print(f"【エラー】{e}")
else:
    # ファイルから1行ずつ読み込んで画面に表示する
    for row in f:
        print(row.strip())

    # ファイルを閉じる
    f.close()
finally:
    print("プログラムを終了します。")