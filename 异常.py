class Student:
    def __init__(self,name,age):
        if not isinstance(name,str):
            raise TypeError('name must be str')
        if not isinstance(age,int):
            raise TypeError('age must be int')

        self.name=name
        self.age=age

    def __str__(self):
        print('打印对象时出发__str__方法')
        return '打印对象时出发__str__方法'


# stu1=Student(4573,'18') # TypeError: name must be str
# stu2=Student('egon','18') # TypeError: age must be int

class PoolEmptyError(Exception): # 可以通过继承Exception来定义一个全新的异常
    def __init__(self,value='The proxy source is exhausted'): # 可以定制初始化方法
        super(PoolEmptyError,self).__init__()
        self.value=value

    def __str__(self): # 可以定义该方法用来定制触发异常时打印异常值的格式
        return '< %s >' %self.value


class NetworkIOError(IOError): # 也可以在特定异常的基础上扩展一个相关的异常
    pass


# raise PoolEmptyError('fucky') # __main__.PoolEmptyError: < The proxy source is exhausted >
# raise NetworkIOError('连接被拒绝') # __main__.NetworkIOError: 连接被拒绝

try:
    s = None
    if s is None:
        print('s是空对象')
        raise NameError('fuck you')
    print(len(s))

except Exception:
    print('空对象没有长度')

# s = None
# if s is None:
#     raise NameError('fuck you')
# # 如果不使用try......except这种形式，那么直接抛出异常，不会执行到这里
# print("is here?")


class PoolEmptyError(Exception): # 可以通过继承Exception来定义一个全新的异常
    def __init__(self,value='The proxy source is exhausted'): # 可以定制初始化方法
        super(PoolEmptyError,self).__init__()
        self.value=value

    def __str__(self): # 可以定义该方法用来定制触发异常时打印异常值的格式
        return '< %s >' %self.value


class NetworkIOError(IOError): # 也可以在特定异常的基础上扩展一个相关的异常
    pass


# raise PoolEmptyError # __main__.PoolEmptyError: < The proxy source is exhausted >
raise PoolEmptyError('被骗了啊') # __main__.PoolEmptyError: < The proxy source is exhausted >
# raise NetworkIOError('连接被拒绝') # __main__.NetworkIOError: 连接被拒绝