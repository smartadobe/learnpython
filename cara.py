class Student:  # 类的命名应该使用“驼峰体”
    def __init__(self, age):
        self.age = age

    school = '清华大学'  # 数据

    @property
    def choose(self):  # 功能
        print('111')

    @choose.setter
    def choose(self,value):
        print("测试定义，类体代码是否执行%s" % value)
        self.age = value


print(Student.__dict__)
print('类方法%s' % id(Student.choose))
# print('类属性%s'%id(Student.school))

st = []
for i in range(3):
    st.append(Student(i))
    print(id(st[i].choose))
    print(st[i].choose)
    print(st[i])

    # print(id(st[i].school))
# class Foo:
#     def __init__(self, val):
#         self.__NAME = val  # 将属性隐藏起来
#
#     @property
#     def name(self):
#         return self.__NAME
#
#     @name.setter
#     def name(self, value):
#         if not isinstance(value, str):  # 在设定值之前进行类型检查
#             raise TypeError('%s must be str' % value)
#             self.__NAME = value  # 通过类型检查后,将值value存放到真实的位置self.__NAME
#
#     @name.deleter
#     def name(self):
#         raise PermissionError('Can not delete')
