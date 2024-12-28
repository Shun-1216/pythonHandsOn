def addin(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum

input = int(input("整数を入力してください"))

print("1から",input,"までの合計は",addin(input),"です。")