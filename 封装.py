class Foo:
    __N=0 # 变形为_Foo__N

    def __init__(self): # 定义函数时，会检测函数语法，所以__开头的属性也会变形
        self.__x=10 # 变形为self._Foo__x

    def __f1(self): # 变形为_Foo__f1
        print('__f1 run')

    def f2(self):  # 定义函数时，会检测函数语法，所以__开头的属性也会变形
        self.__f1() #变形为self._Foo__f1()

# print(Foo.__N) # 报错AttributeError:类Foo没有属性__N

obj = Foo()
# print(obbj.__x) # 报错AttributeError:对象obj没有属性__x

print(Foo.__dict__)
print(obj.__dict__)