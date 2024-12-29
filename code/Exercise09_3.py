"""Exercise09_3.py"""

# キーボードから整数を文字列として入力する
num1 = input("整数1を入力してください：")
num2 = input("整数2を入力してください：")

# 文字列を整数に変換する
try:
    num1 = int(num1)
    num2 = int(num2)

# 四則演算を行い、画面に結果を表示する
    print("整数1 + 整数2 =", num1 + num2)
    print("整数1 - 整数2 =", num1 - num2)
    print("整数1 * 整数2 =", num1 * num2)
    print("整数1 / 整数2 =", num1 / num2)
except ValueError:
    print("【エラー】整数を入力してください。")
except Exception:
    print("【エラー】その他のエラーが発生しました。")