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
print(d.__class__)  # Derived
print('isinstance(d, Derived)', isinstance(d, Derived))  # True
print('issubclass(Base, Derived)', issubclass(Base, Derived))  # False
