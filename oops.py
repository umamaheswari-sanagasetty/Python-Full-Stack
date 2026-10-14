#oops-object oriented programming
#syntax
'''class classname():
    #attributes
    name="uma"
    age=20
    place="vja"
    def fname(method_name):
        print(statements..........)
a=classname()
a.fname()'''

#class declaration
'''class Details():
    name="uma"
    age=20
    place="vja"
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
print(dir(a)) #directories
a.display()'''
    
'''class Details():
    name="uma"
    age=20
    place="vja"
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
a.display()'''

#object instantiation-it can work with single data 
'''class Details():
    def data(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
print(dir(a))
a.data("uma",20,"vja")
a.display()
b=Details()
b.data("deepu",35,"vzg")
b.display()'''

#object initialization-it can work with multiple data
#__init__
'''class Details():
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Details("uma",20,"hyd")
print(dir(a))
a.display()'''

#run time user input
#method 1
'''while True:
    class Details():
        def __init__(self,name,age,place):
            self.name=name
            self.age=age
            self.place=place
        def display(self):
            print(self.name,self.age,self.place)
    a=Details(name=input("enter the name: "),age=int(input("enter the age: ")),place=input("enter the place: "))
    print(dir(a))
    a.display()'''

#method 2
'''while True:
    class Details():
        def __init__(self,name,age,place):  #error
            self.name=input("name")
            self.age=int(input("age"))
            self.place=input("place")
        def display(self):
            print(self.name,self.age,self.place)
    a=Details()        
    print(dir(a))
    a.display()'''
    
'''while True:
    class Details():
        def __init__(self):
            self.name=input("name")
            self.age=int(input("age"))
            self.place=input("place")
        def display(self):
            print(self.name,self.age,self.place)
    a=Details()
    print(dir(a))
    a.display()'''
