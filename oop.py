class employee:
    count=0
    def __init__(self,eid,empname,eage):
        self.eid=eid
        self.name=empname
        self.age=eage
        employee.count=employee.count+1

    def display(self):
        print(self.eid,self.name,self.age)
    def empcount(self):
        print(employee.count)
empObj=employee(123,'ragisha',28)
empObj.display()
empObj1=employee(124, 'ifla', 22)
empObj1.display()
empObj1.empcount()
print(getattr(empObj, "name"))
setattr(empObj, "age", 27)
print(empObj.age)
delattr(empObj,"eid")

print(hasattr(empObj, "eid"))


print(getattr(empObj1, "age"))
setattr(empObj1, "age", 23)
print(empObj1.age)
delattr(empObj1,"age")
# print(empObj1.age)
print(hasattr(empObj1, "name"))