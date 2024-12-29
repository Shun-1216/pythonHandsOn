"""Exercise07_1.py"""


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

    def print_customer(self):
        print("顧客数：",self.customercount)
"""主処理"""
sales1 = Sales("12345","田中太郎",17)
sales1.print_info()
sales1.print_customer()