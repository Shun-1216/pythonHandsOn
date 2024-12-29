"""Exercise07_2.py"""


class Employee:
    """"スーパークラスの定義"""

    def __init__(self, i, n):
        """スーパークラスのコンストラクタ"""
        self.empid = i
        self.empname = n

    def print_info(self):
        """従業員情報を表示するメソッド"""
        print("empid:", self.empid)
        print("empname:", self.empname)

class Sales(Employee):
    def __init__(self,i,n,c):
        """コンストラクタ"""
        super().__init__(i,n)
        self.customercount = c

    def print_info(self):
        super().print_info()
        print("customercount:",self.customercount)

sa = Sales("12345","田中太郎",17)
sa.print_info()