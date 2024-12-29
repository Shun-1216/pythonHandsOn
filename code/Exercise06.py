class Employee:
    companyname = "Python建設株式会社"

    def set_name(self,n):
        self.name = n
    
    def set_age(self,a):
        self.age = a
    
    def add_age(self):
        self.age += 1
    
    def get_info(self):
        return "氏名："+self.name+"、年齢："+str(self.age)
    
    @classmethod
    def get_companyname(cls):
        return cls.companyname
    
print(Employee.companyname)
print(Employee.get_companyname())
emp=Employee()
emp.set_name("豊洲太郎")
emp.set_age(30)
print(emp.get_info())
emp.add_age()
print(emp.get_info())