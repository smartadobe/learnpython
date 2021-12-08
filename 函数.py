x=1

def f1():
    x = 2
    # y = 3
    def f2():
        print('f2的locals%s'%locals())
        print(x)
    print(locals())

    return f2

def f3():
    x=3
    f2=f1() #调用f1()返回函数f2
    print(locals())
    f2()
    print(f2.__closure__)


f3()

