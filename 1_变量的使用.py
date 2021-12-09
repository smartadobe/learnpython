from collections.abc import Iterable


class Array:
    mylist = [0, 1, 2]

    # 返回迭代器类的实例
    def __iter__(self):
        return iter(self.mylist)


# 得到可迭代对象
my_list = Array()
print(isinstance(my_list, Iterable))  # True

for i in my_list:
    print(i)

from functools import reduce

a = reduce((lambda x, y: x + y), [1, 2, 3, 4])
print(a)
