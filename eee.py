#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:           wdf
# datetime:         9/28/2020 8:23 PM
# software:         Windows 10 PyCharm
# file name:        暴力破解rar和zip密码.py
# description:      公众号【特里斯丹】
# usage:
#                   安装所需三方库： pip install zipfile rarfile


class Passward():
    def __init__(self, filename, target_path):
        '''
        :param filename:  待破解的压缩包
        :param target_path:  解压路径
        '''
        self.tatget_path = target_path

        # 根据文件扩展名，使用不同的库
        if filename.endswith('.zip'):
            import zipfile
            self.fp = zipfile.ZipFile(filename)
        elif filename.endswith('.rar'):
            import rarfile
            self.fp = rarfile.RarFile(filename)
        else:
            raise Exception("只支持zip和rar解压。")

    def brutal_extract(self, lengths=[4, ], lower=False, upper=False, digit=False, punctuation=False):
        '''
        # 遍历所有可能的密码，暴力破解
        :param lengths:  密码长度，可以指定所有需要考虑的长度，如[4, 5, 6]等
        :param lower:  是否考虑小写字母
        :param upper:  是否考虑大写字母
        :param digit:  是否考虑数字
        :param punctuation:  是否考虑标点符号
        :return:
        '''
        import string  # 用于生成密码本
        from itertools import combinations_with_replacement  # 用于生成所有可能的密码

        passward_dict = ""
        if lower:
            passward_dict += string.ascii_lowercase
        if upper:
            passward_dict += string.ascii_uppercase
        if digit:
            passward_dict += string.digits
        if punctuation:
            passward_dict += string.punctuation

        print("密码本：\t{}\n密码长度：\t{}\n".format(passward_dict, lengths))
        count = 0

        for length in lengths:
            pwd = combinations_with_replacement(passward_dict, length)
            for passward in pwd:
                passward = "".join(passward)
                count += 1
                if self.extract(passward):
                    print()
                    print("一共尝试了{}种可能".format(count))
                elif self.extract(111000111000):
                    print('111000撞库成功')
                elif self.extract(222111111000):
                    print('222111撞库成功')
                    return
            print("对不起，暂未找到，请尝试：\n1. 其他密码长度\n2. 包含更多种类的密码字符")

    def extract(self, passward):
        try:
            self.fp.extractall(path=self.tatget_path, pwd=passward.encode())
            print()
            print('成功破解该压缩包，密码为： ' + passward)
            self.fp.close()
            return True
        except:
            pass


def main():
    x = Passward(filename="C:\\Users\\016456310\\Desktop\\我和我的F辈.无水印中字版.zip", target_path="C:\\Users\\016456310\\Desktop")
    x.brutal_extract([1,], digit=True, lower=False, upper=False, punctuation=False)


if __name__ == '__main__':
    main()