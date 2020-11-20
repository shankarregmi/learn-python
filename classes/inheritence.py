class Base:
    def func1(self):
        print('Base Class Func 1')
    
    def func2(self):
        print('Base Class Func 2')
        self.func1()

class Derived(Base):
    def func1(self):
        print('Derived Class Func 1')

d = Derived()

d.func2()