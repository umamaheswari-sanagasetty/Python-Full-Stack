#difference b/w _ and __
#emp1
'''class Employee1():
    def __init__(self):
        self.name="uma"
        self._mailid="uma@gmail.com"
        self.__salary=20000 #private variable
a=Employee1()
print(dir(a))
print(a.name)
print(a._mailid)
#print(a.__salary)   #error
print(a._Employee1__salary)'''

#emp1&2
'''class Employee1():
    def __init__(self):
        self.name="uma"
        self._mailid="uma@gmail.com"
        self.__salary=20000 #private variable
class Employee2():
    def __init__(self):
        self.name="mahi"
        self._mailid="mahi@gmail.com"
        self.__salary=25000 #private variable
a=Employee1()
print(dir(a))
print(a.name)
print(a._mailid)
#print(a.__salary)  #error
print(a._Employee1__salary)
b=Employee2()
print(dir(b))
print(b.name)
print(b._mailid)
#print(b.__salary)  #error
print(b._Employee2__salary)'''

#polymorphism
#operator overloading
'''a=2;b=4
print(a+b)
print(a.__add__(b))
print(a.__add__(8))
print(a.__sub__(1))
print(a.__mul__(5))
#print(a.__div__(2))
print(a.__pow__(4))
print(a.__ge__(10))
print(a.__le__(20))
a=[1,2,3,4,5];b=[6,7,8,9,10]
print(a.__add__(b))
print(a.__getitem__(3))
print(a.__getitem__(4))
a="code";b="gnan"
print(a.__add__(b))
a="python";b="course"
print(a.__add__(b))
print(a.__add__(" "+b))
print(a.__add__(" "+b).title())
print("uma".__add__("s"))'''

#operator overriding
'''class A():
    def __init__(self,a):
        self.a=a
    def __add__(self,value):
        return self.a*value.b
class B():
    def __init__(self,b):
        self.b=b
x=A(10)
y=B(20)
#x=10
#y=20
print(x+y)'''

#method overloading
'''class new():
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print("the sum is",a+b+c)
        elif a!=None and b!=None:
            print("the product is",a*b)
        else:
            print("program ends.......")
a=new()
a.sum()
a.sum(2,3,4)
a.sum(5,4)'''

'''class new():
    def sum(self,a=4,b=5,c=6):
        if a!=5 and b!=6 and c!=7:
            print("the sum is",a+b+c)
        elif a!=5 and b!=6:
            print("the product is",a*b)
        else:
            print("program ends.......")
a=new()
a.sum()'''

#method overriding
'''class Animal():
    def speak(self):
        print("animal can make sounds")
class Dog():
    def speak(self):
        print("dog barks")
a=Animal()
b=Dog()
a.speak()
b.speak()'''

#vehicle
'''class Car():
    def vehicle(self):
        print("Thar")
class Bike():
    def vehicle(self):
        print("Shine")
a=Car()
b=Bike()
a.vehicle()
b.vehicle()'''
