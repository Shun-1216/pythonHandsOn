month = int(input("1～12の整数を入力してください："))

if(month>=3 and month<=5):
    print("春です。")
elif(month>=6 and month<=8):
    print("夏です。")
elif(month>=9 and month<=11):
    print("秋です。")
elif(month==12 or month==1 or month==2):
    print("冬です。")
else:
    print("1～12の整数を入力してください")

