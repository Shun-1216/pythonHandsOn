price = input("金額を入力してください")
volume = input("個数を入力してください")
amount=int(price)*int(volume)
print("\n金額\\{:,}\t個数：{:,}\t合計金額：\\{:,}".format(int(price),int(volume),amount))