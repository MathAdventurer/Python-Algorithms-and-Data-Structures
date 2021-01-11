#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: Wang,Xudong 220041020 SDS time:2020/11/25

class Fraction:
    def gcd(m: int, n: int):
        if n != 0 and m != 0:
            while m % n != 0:
                oldm = m
                oldn = n
                m = oldn
                n = oldm % oldn
            return n
        else:
            return None

    def __init__(self,top,bottom):
        common = Fraction.gcd(top, bottom)
        self.num = top//common
        self.den = bottom//common

    def show(self):
        print(self.num,"/",self.den)
        print(self.num,"/",self.den)

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    # 定义加法  \为续行符
    # def __add__(self, otherfraction):
    #     newnum = self.num * otherfraction.den + \
    #              self.den * otherfraction.num
    #     newden = self.den * otherfraction.den
    #     return Fraction(newnum,newden)
    # 化简分数的方法 greatest common divisor，GCD
    # 欧几里得算法 化简分数 不用loop用判断写不出来

    def __add__(self,otherfraction):
        newnum = self.num * otherfraction.den + \
                 self.den * otherfraction.num
        newden = self.den * otherfraction.den
        common = Fraction.gcd(newnum,newden)   #如果函数定义在class内部，调用的时候需要用class.method,定义在外部可以直接调用gcd
        return Fraction(newnum//common,newden//common) #只取了余数

    # 浅相等与真相等
    # 浅相等：同一个对象的引用(根据引用来判断)才为真,在当前实现中，分子和分母相同的两个不同的对象是不相等的。
    # 深相等：根据值来判断相等，而不是根据引用
    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = self.den * other.num
        return firstnum == secondnum

    def __le__(self, other):
        firstnum = self.num * other.den
        secondnum = self.den * other.num
        return firstnum <= secondnum


if __name__ == "__main__":
    f1 = Fraction(6,8)
    f1.show()
    print(f1)
