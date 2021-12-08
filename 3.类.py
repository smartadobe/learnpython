class Student:
    school='清华大学'

    #该方法会在对象产生之后自动执行，专门为对象进行初始化操作，可以有任意代码，但一定不能返回非None的值
    def __init__(self,name,sex,age):
        self.name=name
        self.sex=sex
        self.age=age

    def choose(self):
        print('%s is choosing a course' %self.name)


# def asshole ():
#     return Student
#
# a = asshole()
# print(a)
# print(type(a))
# print(a.__dict__)
st1 = Student()
print(Student.__name__)
