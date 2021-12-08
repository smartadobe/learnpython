print('开始导入eee模块')
import eee
print('结束导入eee模块')
x=1
y = [1,2]
def get():
    print(x)
def change():
    global x
    x=0
    y.append(3)
class Foo:
    def func(self):
       print('from the func')
print(x)
print(y)
change()
print('---------------')
print(x)
print(y)
print('foo模块名称空间包括：',globals())
