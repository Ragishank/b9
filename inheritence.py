class cal1:
    def mul(self,a,b):
        return a*b
class cal2:
    def su(self,a,b):
        return a+b


class cal3(cal1,cal2):
    def di(self,a,b):
        return a/b

d=cal3()
print(d.di(10,20))
print(d.su(30,3))



