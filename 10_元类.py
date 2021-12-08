"""
对象实例化的过程分三步：
1、调用类中__new__方法，创建一个空对象obj
2、调用类中__init__方法，将空对象obj，连同其他相关参数传入，完成对象的初始化
3、返回初始化后的obj

在调用一个对象时，会调用这个对象所在类的__call__方法
"""


# a)class关键字的机制：类名、基类、类的名称空间

# class Mymeta(type):
#     def __init__(self,class_name,class_bases,class_dic):
#         print(self.__dict__)
#
# class People(object,metaclass=Mymeta):
#     school = 'UIBE'
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         print('OK')
#     def say(self):
#         print('欢迎%s加入%s大家庭'%(self.name,self.school))
#
# class_name = 'People'
# class_bases = (object,)
# class_dic = {}
# classstr = """
# school = 'UIBE'
# def __init__(self,name,age):
#     self.name = name
#     self.age = age
#     print('OK')
# def say(self):
#     print('欢迎%s加入%s大家庭'%(self.name,self.school))
# """
# exec (classstr,{},class_dic)
# print('---------------')
# Mymeta(class_name,class_bases,class_dic)

# b)自定义类的创建
# class Mymeta(type):
#     def __init__(self,class_name,class_bases,class_dic):
#         # print(self.__dict__)
#         # print(class_name)
#         # print(class_bases)
#         # print(class_dic)
#         if class_name.islower():
#             raise TypeError('类名字必须是驼峰体')
#         if "__doc__" not in class_dic or len(class_dic['__doc__'].strip('\n'))==0:
#             raise TypeError('类中必须要要有注释')
# class People(metaclass=Mymeta):
#     """
#     此文档是People类的注释文档
#     """
#     school = 'UIBE'
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         print('OK')
#     def say(self):
#         print('欢迎%s加入%s大家庭'%(self.name,self.school))


# #c)自定义元类，控类的调用
# class Mymeta(type):
#     def __call__(self, *args, **kwargs):
#         print('run.....')
#         print(self)
#         obj = self.__new__(self)
#         self.__init__(obj,*args, **kwargs)
#         return obj
#     def __init__(self,class_name,class_bases,class_dic):
#         # print(self.__dict__)
#         # print(class_name)
#         # print(class_bases)
#         # print(class_dic)
#         if class_name.islower():
#             raise TypeError('类名字必须是驼峰体')
#         if "__doc__" not in class_dic or len(class_dic['__doc__'].strip('\n'))==0:
#             raise TypeError('类中必须要要有注释')
# class People(metaclass=Mymeta):
#     """
#     此文档是People类的注释文档
#     """
#     school = 'UIBE'
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         print('OK')
#     def say(self):
#         print('欢迎%s加入%s大家庭'%(self.name,self.school))
#
#
# tailu = People('邰禄',28)
# print(tailu.school)

# d)属性查找顺序


class Mymeta(type):  # 只有继承了type类才能称之为一个元类，否则就是一个普通的自定义类
    n = 444

    def __new__(cls, a, b, c):
        obj = type.__new__(cls, a, b, c)  # 必须按照这种传值方式
        print(obj.__dict__)
        print(obj.n)
        return obj  # 只有在返回值是type的对象时，才会触发下面的__init__
        # return 123

    def __init__(self, class_name, class_bases, class_dic):
        print('run。。。')


class StanfordTeacher(object, metaclass=Mymeta):  # StanfordTeacher=Mymeta('StanfordTeacher',(object),{...})
    n = 111

    school = 'Stanford'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        print('%s says welcome to the Stanford to learn Python' % self.name)


print(type(Mymeta))  # <class 'type'>
# 产生类StanfordTeacher的过程就是在调用Mymeta，而Mymeta也是type类的一个对象，那么Mymeta之所以可以调用，一定是在元类type中有一个__call__方法
# 该方法中同样需要做至少三件事：
# class type:
#     def __call__(self, *args, **kwargs): #self=<class '__main__.Mymeta'>
#         obj=self.__new__(self,*args,**kwargs) # 产生Mymeta的一个对象
#         self.__init__(obj,*args,**kwargs)
#         return obj
