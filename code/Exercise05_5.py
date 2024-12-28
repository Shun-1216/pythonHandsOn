def deco(func):
    def wrapper(n):
        print("---関数の処理を開始します---")
        print(func)
        func(n)
        print("---関数の処理を終了します---")
    return wrapper

@deco
def do_some_loop(n):
    for i in range(n):
        print(i)

do_some_loop(5)