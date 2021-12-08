#三元表达式
x = 1;y = 2
res = '我赢了' if x>y else '你赢了'
print(res)

#列表生成式
l1 = [i for i in range(10) if i%2==0]
print(l1)

#for循环嵌套
l2 = [i**2 for  i in range(10) if i%2==0  for j in range(10) if j+i>5]
print(l2)

#生成器表达式，只需要把列表生成式中的[]换成()
g1 = (i for i in range(10) if i%2==0)
print(g1)
print(next(g1))
print(g1.__next__())

lm1 = max({'zhanglei':18,"wangpao":20,"ase":30},default=100,key=lambda k:{'zhanglei':18,"wangpao":20,"ase":30}[k])
print(lm1)