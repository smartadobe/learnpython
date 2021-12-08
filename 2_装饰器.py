import time

#无参装饰器，timer，用来计算函数的执行时间
def timer(func):
        def wrapper(*args,**kwargs):
            start_time = time.time()
            res = func(*args,**kwargs)
            time.sleep(0.8)
            end_time = time.time()
            return res,end_time-start_time
        wrapper.__name__ = func.__name__
        wrapper.__doc__ = func.__doc__
        return wrapper

#有参数装饰器，barker，用来控制参数获取方式
def barker(style):

    def timer(func):

        def wrapper(*args, **kwargs):
            if style == 'wenjian':
                res = func(*args, **kwargs)
                time.sleep(0.8)
            if style == 'wangluo':
                print('我要睡四秒钟')
                res = func(*args, **kwargs)
                time.sleep(4)
            return res

        return wrapper

    return timer


#装饰器，打印当前系统时间
def realtime(f1):
    def wrap(*args,**kwargs):
        print(time.strftime('%Y%m%d'))
        res = f1(*args,**kwargs)
        return res
    return wrap


#add = realtime(timer(add))
@realtime
@ timer
#被装饰函数
def add(x,y):
    """

    :param x:变量1
    :param y: 变量2
    :return: 返回两个变量的和
    """
    return x+y

#有参数装饰器
@barker(style='wangluo')
def foo(x):
    print('%s我是你爸爸'%x)


if __name__ == '__main__':
    print(add(1,2))
    foo('帅哥')
    help(add)