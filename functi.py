#non parametrised
def fnName():
    a=20
    print(a)
fnName()
#noraml method parametrerized
def fnName1(name,age,place,dob):
    print(n)
fnName("chethan",18,"kozhikode","")

#defualt argument

def fnName2(name,place,age=18):
    print(name,age,place)
fnName2("chethan","clt",20)

#variable length
def fnName3(*a):
    print(a)
fnName3(1,2,5,6,86)
fnName3(4,2,4)

#keyword

def fnName4(**a):
    print(a)

fnName4(name="chethan",no=12343343,age=18,place="clt"

a=lambda x:x+20
print(a(30))
