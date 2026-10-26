#inheritance
#single-inheritance
'''class RBI(): #parent class
    cash=100000
    def available_cash(cls):
        print("available cash is",cls.cash)
        print("available cash is",RBI.cash)
class SBI(RBI): #child 1
    pass
class HDFC(RBI): #child 2
    cash=50000
    def new_cash(cls):
        print("new cash is",cls.cash+cls.cash)
        print("new cash is",cls.cash+RBI.cash)
a=HDFC()
a.available_cash()
a.new_cash()'''

#multiple inheritance
#without inherit properties from parent classes
'''class Father(): #parent-1
    def height(self):
        print("5.5 inches")
class Mother(): #parent-2
    def weight(self):
        print("60 kgs")
class Kid(): #child
    def dob(self):
        print("just born....")
a=Father()
b=Mother()
c=Kid()
a.height()
b.weight()
c.dob()'''

#inherit properties from parent classes
'''class Father(): #parent-1
    def height(self):
        print("5.5 inches")
class Mother(): #parent-2
    def weight(self):
        print("60 kgs")
class Kid(Father,Mother): #child
    def dob(self):
        print("just born....")
c=Kid()
c.height()
c.weight()
c.dob()'''

#multi-level inheritance
'''class Grand_Parents():
    def land(self):
        print("4 acres")
class Parents(Grand_Parents):
    def house(self):
        print("500 square feet")
class Child(Parents):
    def car(self):
        print("Tokyo")
a=Child()
a.land()
a.house()
a.car()'''

#hierarchical inheritance
'''class employee(): #parent
    def company(self):
        print("HCL")
class trainer(employee): #child-1
    def teach(self):
        print("the trainer teaches the course")
class developer(employee): #child-2
    def code(self):
        print("the developer develops the code")
a=trainer()
b=developer()
a.company()
a.teach()
b.company()
b.code()'''

#hybrid inheritance
'''class trainer(): #parent
    def teach(self):
        print("trainer teaches the course")
class developer(trainer): #child-1
    def code(self):
        print("developer develops the code")
class student(trainer): #child-2
    def study(self):
        print("student studies the course")
class program_manager(student,developer): #grand_child
    def work(self):
        print("program manager manages the work")
a=program_manager()
a.teach()
a.code()
a.study()
a.work()'''

#super()
'''class parent():
    def __init__(self,name):
        self.name=name
        print("parent constructor")
class child(parent):
    def __init__(self,name,city):
        super().__init__(name)
        self.city=city
        print("child constructor")
a=child("uma","vja")
print(a.name)
print(a.city)'''
