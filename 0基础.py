# a = 'ni hao a '
# b = '你好啊'
# print(a)
# print(b)
# l1 = list(a)
# l1.insert(0,1)
# print(l1)
# d1 = {'name':'zhanglei', 'age':18}
# for key in d1.items():
#     print(key)
#
# d1.pop()

# with open(r'C:\Users\016456310\Desktop\123.jpg',mode='rb') as f:
#     # a = f.read()
#     # b = a.decode('utf-8') #因为文件是图片，原文件不存在字符编码的问题，所以解码就会报错
#     # print(type(a))
#     # print(a)
#     # print(b)
#     for line in f:
#         print(line)
#     print(f.name)
#     # f.writelines((b'123\n', 'abc'.encode('utf-8')))
#     f.seek(2,0)
#     print('当前所在位置：%s'%f.tell())
#     a = f.read()
#     print(a)
#     f.writable()

#t模式
# with open(r'C:\Users\016456310\Desktop\主线.txt',mode='r', encoding='gbk') as f:
#     a = f.read(3)#移动的是3个字符
#     print(a)
#     b = f.read(10)
#     print(b)
#     f.seek(29,0)
#     c = f.read(10)
#     print(c)
#b模式
# with open(r'C:\Users\016456310\Desktop\主线.txt',mode='rb') as f:
#     a = f.read()#移动的是3Bytes
#     print(a.decode('gbk'))
#     f.seek(7,0)
#     print(f.tell())
#     line1 = f.readline()
#     print(line1.decode('gbk'))

#打开一个gbk编码的文件，将里面的内容复制到另外一个文件中，编码格式是utf8
with open(r'C:\Users\016456310\Desktop\主线.txt',mode='rb') as read_f, open(r'C:\Users\016456310\Desktop\主线1.txt',mode='wb') as write_f:
    # b = read_f.read()
    print(read_f.tell())
    read_f.seek(0,0)
    # a = read_f.read().decode('gbk').encode('utf-8')
    # write_f.write(a)
    print(write_f.tell())

with open(r'C:\Users\016456310\Desktop\主线1.txt',mode='rb') as f:
    f.read(7)
    f.read(3)
    line1 = f.readline().decode('utf-8')

    print(line1)
def cara(ddd,x=1):
    woshijubu = 'jubu'
    print('局部变量：%s'%locals())
    print('全局变量：%s'%globals())
cara(1)
print(locals())

print(globals())

