# -*- coding: utf-8 -*-
# @Time    : 17-10-20 下午9:34
# @Author  : shitouBoy
# @Email   : xy960722@gmail.com
# @File    : module.py
# @Describe:
# @Software: PyCharm

class Calculator():
    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b
    def mul(self):
        return self.a * self.b
    def div(self):
        return self.a / self.b
