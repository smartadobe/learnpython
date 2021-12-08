# f=open('a.txt','r',encoding='gbk')
# data=f.read()
# print(data)
# # f.close()
# # print(globals())
# # print(f)
#
# a,b = 'user:password'.split(':')
# print(a)
# print(b)

with open(r'c.txt',mode='wb') as f:
    f.write('噩噩\n'.encode('utf-8'))
    f.writelines(['333\n'.encode('utf-8'), bytes('444\n',encoding='utf-8'),bytes('444\n',encoding='utf-8')])
    f.