import random


def create_phone():
    # 第二位数字
    second = [3, 4, 5, 7, 8][random.randint(0, 4)]

    # 第三位数字
    third = {
        3: random.randint(0, 9),
        4: [5, 7, 9][random.randint(0, 2)],
        5: [i for i in range(10) if i != 4][random.randint(0, 8)],
        7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
        8: random.randint(0, 9),
    }[second]

    # 最后八位数字
    suffix = random.randrange(10000000,100000000)

    # 拼接手机号
    return "1{}{}{}".format(second, third, suffix)

# 生成手机号
with open('c.txt',mode='w',encoding='utf-8') as f:
    i = 0
    while i<=100:
        phone = create_phone()
        f.write('{}\n'.format(phone))
        i+=1


with open('phone.txt',mode='w',encoding='utf-8') as f:
    f.write('15611551397\n')
    f.write('13381120817\n')
    f.write('13884771301\n')
    f.write('13455051091\n')
    f.write('15022065226\n')
    f.write('18613309497\n')
    f.write('13863280121\n')
    f.write('15026829883\n')

