#1、定制化元类，使得自定义类属性为大写
import setting

class Mymeta2(type):
    def __new__(cls, name, bases, dic):
        dic_new = {}
        print('.................%s'%cls.__dict__)
        print(cls)
        for k,v in dic.items():
            if not callable(v) and not k.startswith('__'):
                dic_new[k.upper()] = v
            else:
                dic_new[k] = v
        return type.__new__(cls, name, bases, dic_new)
        # return 123

    def __init__(self,name,bases,dic):
        print(self.__dict__)
        print(dic)
        dic_new = {}
        for k, v in dic.items():
            if not callable(v) and not k.startswith('__'):
                dic_new[k.upper()] = v
            else:
                dic_new[k] = v
        # print(dic_new) # 属性已经变成大写了
        # self.__dict__ = dic_new  #AttributeError: attribute '__dict__' of 'type' objects is not writable
        super(Mymeta2, self).__init__(name,bases,dic_new) #这种方式也不行,因为在init方法之前，type的__call__方法中，self.__new__的时候属性已经存在了。



class Language(metaclass=Mymeta2):
    lang = 'chinese'
    guo_gi = 'china'
    def __init__(self,name,age):
        self.name =name
        self.age = age

    def say(self):
        print('姓名：%s，年龄：%s' % (self.name, self.age))

# a = Language('zhanglei',30)
# print(a.__dict__)
# a.say()
# print(Language.__dict__)


#2、定制化元类，更改自定义类的对象数据属性为隐藏属性
class Mymeta1(type):
    def __call__(self, *args, **kwargs):
        obj = self.__new__(self)
        self.__init__(obj,*args, **kwargs)
        obj.__dict__ = {'_%s__%s'%(self.__name__,k):v for k,v in obj.__dict__.items()}
        return obj

class Mather(metaclass=Mymeta1):

    def __init__(self,name,age):
        self.name = name
        self.age = age
        print('姓名：%s，年龄：%s' % (self.name, self.age))


    def say(self):
        print('姓名：%s，年龄：%s' % (self.name, self.age))

# stu = Mather('zhanglei',30)
# stu.say() #属性隐藏之后，调用函数报错
# print(stu.__dict__)




#3、定制化元类，是的自定义类中不需要__init__方法,且实例化时必须要通过关键字参数方式赋值。
class Mymeta0(type):
    def __call__(self, *args, **kwargs):

        obj = self.__new__(self)

        if args:
            print('必须要用使用关键字参数赋值方式进行实例化')
        else:
            obj.__dict__ = {k:v for k,v in kwargs.items()}
        return obj


class Financer(object,metaclass=Mymeta0):
    school = 'UIBE'

    def tellinfo(self):
        print('学校的名字是:%s'%self.school)

# f_obj = Financer(name = 'zhanglei', age = 30, sex = 'male')
# f_obj = Financer('zhanglei', 30, 'male', age = 30, sex = 'male')
# print(f_obj.school)
# f_obj.tellinfo()
# print(f_obj.__dict__)





#4、定制化元类，实现单例模式（每次实例，都指向相同的内存地址，避免占用过多内存）
#setting.py配置文件中存储了host和port
# 1)通过类方法实现
import setting

class Single:
    __instance = None

    def __init__(self,host,port):
        self.host = host
        self.port = port


    @classmethod
    def singleton(cls):
        if not cls.__instance:
            cls.__instance = cls(setting.HOST, setting.PORT)
        return cls.__instance

# a = Single('192.168.1.1','9080')
# b = Single('192.168.1.1','9080')
# print(a is b)
# c = Single.singleton()
# d = Single.singleton()
# print(c is d)

# 2)定制元类，实现单例模式

class Mymeta4(type):


    def __init__(self, name, bases, dic):  # 定义类Sig时就触发
        # 事先先从配置文件中取配置来造一个Sig的实例出来
        print(self.__dict__)
        self.__instance = object.__new__(self)  # 产生对象
        self.__init__(self.__instance, setting.HOST, setting.PORT)  # 初始化对象
        # 上述两步可以合成下面一步

        # super().__init__(name, bases, dic)

    def __call__(self, *args, **kwargs):  # Sig(...)时触发
        if args or kwargs:  # args或kwargs内有值
            obj = object.__new__(self)
            self.__init__(obj, *args, **kwargs)
            return obj
        return self.__instance

class Sig(metaclass=Mymeta4):
    def __init__(self,host,port):
        self.host = host
        self.port = port

e = Sig('192.168.1.1','9080')
f = Sig('192.168.1.1','9080')
print(e is f)

g = Sig()
h = Sig()
print(g is h)
print(Sig.__dict__)

