"""company.py"""


class Employee:
    """"スーパークラスの定義"""

    def __init__(self, i, n):
        self.empid = i
        self.empname = n

    def print_info(self):
        print("empid:", self.empid)
        print("empname:", self.empname)


class Sales(Employee):
    """"サブクラスの定義"""

    def __init__(self, i, n, c):
        super().__init__(i, n)
        self.customercount = c

    def print_customer(self):
        print("顧客数:", self.customercount)
