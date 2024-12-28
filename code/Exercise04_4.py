product={"HS":"ハサミ","CT":"カッター","DR":"ドライバー","SP":"スパナ"}
print(product)

key=input("キーを入力してください")

if key in product:
    print("値：",product[key])
else:
    print("入力したキーは含まれていません")