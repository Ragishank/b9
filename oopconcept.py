# class Employee:
#     name="chethan"
#     age=18
#     ad_no=1243435
#     gender="male"
#     def display(self):
#         print(self.name,self.age,self.ad_no,self.gender)

# empObj=Employee()
# empObj.display()

class Employee:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
empObj1=Employee("chethan", 18, "clt")
empObj1.display()
empObj2=Employee("ragisha", 27,"clt")
empObj2.display()


