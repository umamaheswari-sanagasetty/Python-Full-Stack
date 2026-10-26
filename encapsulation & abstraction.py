#encapsulation
#publicdata
'''class A():
    publicdata=10
    def method1(self):
        print("method1 is implemented")
class B(A):
    def method2(self):
        print("method2")
x=B()
x.method1()
x.method2()'''

'''class A():
    publicdata=10
    def method1(self):
        print(self.publicdata)
class B(A):
    def method2(self):
        print(self.publicdata)
x=B()
x.method1()
x.method2()'''

#_protecteddata
'''class A():
    _protecteddata=100
    def method1(self):
        print(self._protecteddata)
class B(A):
    def method2(self):
        print(self._protecteddata)
x=B()
x.method1()
x.method2()
print(x._protecteddata)'''

#__privatedata
'''class A():
    __privatedata="uma"
    def method1(self):
        print(self.__privatedata)
class B(A):
    def method2(self):
        print(self._A__privatedata)
y=B()
y.method1()
y.method2()
print(y._A__privatedata)'''

#abstraction
'''class A():
    def method1(self):
        pass
obj1=A()
obj1.method1()'''

'''class A():
    def method1(self):
        print("data")
obj1=A()
obj1.method()'''

'''from abc import ABC,abstractmethod
class A(ABC):
    def method1(self):
        print("python")
obj1=A()
obj1.method1()'''

'''from abc import ABC,abstractmethod
class A():
    @abstractmethod
    def method1(self):
        print("python")
obj1=A()
obj1.method()'''#error

'''from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def method1(self):
        pass
    def method2(self):
        print("method2 is implemented")
    @abstractmethod
    def method3(self):
        pass
class B(A):
    def method1(self):
        print("method1 is implemented")
    def method3(self):
        print("method3 is implemented")
obj1=B
obj1.method1()
obj1.method2()
obj1.method3()'''
