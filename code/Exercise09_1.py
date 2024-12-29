f = open("code/input.txt","r",encoding="utf-8")
i=1

for row in f:
    print(f"{i}行目：{row.strip()}")
    i +=1
f.close