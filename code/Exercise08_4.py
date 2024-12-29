import re
city = ["江東区","品川区","横浜市","豊島区","川崎市"]

print("市区のリスト：\n"+str(city)+"\n区=○")

pattern=".+区$"
regex = re.compile(pattern)

for c in city:
    if regex.search(c)==None:
        result = "✕"
    else:
        result = "○"
    print("\t"+c+":"+result)