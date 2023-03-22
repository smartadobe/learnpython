class Mymeta(type): #只有继承了type类才能称之为一个元类，否则就是一个普通的自定义类
    """
    因为type中__call__时候，一定是先self.__new__再调用self.__init__的，最后返回初始化的“对象”，所以控制自定义类的时候，可以在__new__方法中，也可以在__init__方法中,
    但是如果控制自定义类的属性，比如改成大写，或者改为隐藏属性，那么必须要在__new__方法中，在__init__方法中不可以，因为在__new__之后，类的属性已经存在。
    """
    # def __new__(cls, class_name,class_bases,class_dic):
    #
    #     if class_name.islower():
    #         raise TypeError('类名%s请修改为驼峰体' %class_name)
    #
    #     if '__doc__' not in class_dic or len(class_dic['__doc__'].strip(' \n')) == 0:
    #         raise TypeError('类中必须有文档注释，并且文档注释不能为空')
    #
    #     return type.__new__(cls,class_name,class_bases,class_dic)

    def __init__(self,class_name,class_bases,class_dic):
        print(self) #<class '__main__.StanfordTeacher'>
        print(self.__dict__)
        print(class_bases) #(<class 'object'>,)
        print(class_dic) #{'__module__': '__main__', '__qualname__': 'StanfordTeacher', 'school': 'Stanford', '__init__': <function StanfordTeacher.__init__ at 0x102b95ae8>, 'say': <function StanfordTeacher.say at 0x10621c6a8>}

        # super(Mymeta, self).__init__(class_name, class_bases, class_dic)  # 重用父类的功能
        # super().__init__(self) # 也可以用这种方式。   注意！！甚至都可以不需要调用super().__init__方法进行初始化。猜测：type的__call__方法中，最后一定是补充调用了自己的__init__方法

        if class_name.islower():
            raise TypeError('类名%s请修改为驼峰体' %class_name)

        if '__doc__' not in class_dic or len(class_dic['__doc__'].strip(' \n')) == 0:
            raise TypeError('类中必须有文档注释，并且文档注释不能为空')


    # def __call__(self, *args, **kwargs):
    #     obj = self.__new__(self)
    #     print(obj.__dict__)#此时对象是空对象，这个和type中的__call__方法不同！！！
    #     self.__init__(obj,*args, **kwargs)
    #     print(obj.__dict__)#此时对象经过初始化之后，已经有属性了，不在是空对象了。
    #
    #     return obj



# StanfordTeacher=Mymeta('StanfordTeacher',(object),{...})
class Stanfordteacher(object,metaclass=Mymeta):
    """
    类StanfordTeacher的文档注释
    """
    school='Stanford'

    def __new__(cls, *args,**kwargs):
        print(args)
        # name_new,age_new = str(name).upper(),str(age).upper()
        args_new = [str(k).upper() for k in args]
        return super().__new__(cls)


    def __init__(self,name,age):
        print(self)
        print(self.__dict__)#此时对象self是个空对象。
        self.name=name
        self.age=age


    def say(self):
        print('%s says welcome to the Stanford to learn Python' %self.name)

a = Stanfordteacher('zhanglei',30)
print(a.__dict__)