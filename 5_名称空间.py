def scope_test():

    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam  # 当外层作用域不存在spam名字时，nonlocal不能像global那样自作主张定义一个
        spam = "nonlocal spam"  # free variable spam经nonlocal声明后，可以做重绑定操作了，可写的。

    def do_global():
        global spam  # 即使全局作用域中没有名字spam的定义，这个语句也能在全局作用域定义名字spam
        spam = "global spam"  # 自有变量spam经global声明后，可以做重绑定操作了，可写的。

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)


# def deco():
#     age = 10
#     def wrapper():
#         def adobe():
#             nonlocal age
#             age += 1
#             print(age)
#         print(age)
#         return adobe
#     return wrapper
#
# deco()()()
if __name__=='__main__':
    scope_test()

    print(globals())
