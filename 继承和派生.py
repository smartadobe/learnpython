# class ParentClass1: #定义父类
#     def __str__(self):
#         # print('测试打印对象会不会出发这个方法')
#         return '测试打印对象会不会出发这个方法'
#
# class ParentClass2: #定义父类
#     pass
#
# class SubClass1(ParentClass1): #单继承
#     pass
#
# class SubClass2(ParentClass1,ParentClass2): #多继承
#     pass
#
# print(SubClass2.__base__)
# print(SubClass2.__bases__)
# print(ParentClass1.__bases__)
# print(ParentClass1())

class Foo:
    def f1(self):
        print('Foo.f1')

    def f2(self):
        print('Foo.f2')
        self.f1()

class F1(Foo):
    def f1(self):
        print('F1.f1')

b = Foo()
b.f2()
print('------')
c = F1()
c.f2()


#隐藏父类中的方法
class Bar:
    def __f1(self):
        print('Bar.f1')

    def f2(self):
        print('Bar.f2')
        self.__f1()

class Car(Bar):
    def __f1(self):
        print('Car.f1')

b = Bar()
b.f2()
print('------')
c = Car()
c.f2()

print(Car.mro())

