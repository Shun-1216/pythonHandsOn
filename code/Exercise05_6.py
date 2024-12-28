"""Exercise05_6.py"""


def odd_generator():
    """奇数を1つずつ返すジェネレータの関数"""
    i = 1

    while True:
        # i が奇数の場合、yield文で i を戻り値として返す
        # i の値は、次回の関数呼び出しのために保持される
        if i % 2 != 0:
            yield i
        i = i + 1

# ジェネレータをイテレータとして取得
gen = odd_generator()
# next関数にジェネレータの変数を引数として渡してジェネレータの関数を呼び出す
print(next(gen))
print(next(gen))
print("休憩")
print(next(gen))