"""Exercise06_4.py"""


class Employee:
    """従業員クラス"""

    def __init__(self,n,a):
        """コンストラクタ"""
        self.name = n
        self.age = a

    def set_name(self, n):
        """氏名を設定するメソッド"""
        self.name = n

    def set_age(self, a):
        """年齢を設定するメソッド"""
        self.age = a

    def add_age(self):
        """年齢を1つ増やすメソッド"""
        self.age += 1

    def get_info(self):
        """従業員情報の文字列を返すメソッド"""
        return "氏名:" + self.name + "、年齢:" + str(self.age)

emp=Employee("田中太郎",27)
print(emp.get_info())
emp.add_age()
print(emp.get_info())