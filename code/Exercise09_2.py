str=input("書き込む文字列を入力してください：")
line=int(input("書き込む行数を整数で入力してください："))

with open("code/output.txt","w",encoding="utf-8") as f:
    for i in range(line):
        f.write(f"{i+1}回目：{str}\n")