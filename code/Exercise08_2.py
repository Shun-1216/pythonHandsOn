str1 = input("文字列を入力してください")
str2 = input("検索する文字列を入力してください")

i = str1.find(str2)

if i < 0:
    print("見つかりませんでした")
else:
    print("開始位置："+str(i))