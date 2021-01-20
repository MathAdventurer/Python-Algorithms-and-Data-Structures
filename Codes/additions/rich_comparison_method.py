#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: Wang,Xudong 220041020 SDS time:2021/1/20
"""
Python中的富比较运算符


摘要：
This PEP proposes several new features for comparisons:
Allow separately overloading of <, >, <=, >=, ==, !=, both in classes and in C extensions.
Allow any of those overloaded operators to return something else besides a Boolean result.

重写 C extensions中比较运算符
允许重写的比较运算符返回除布尔运算符之外的其他结果

动机/用途：
例如 numpy中对于array的比较大小需要进行扩展
某些缺少顺序的结构的比较
不同类型之间的对象，按照一定次序进行比较



Classes can define new special methods __lt__, __le__, __eq__, __ne__, __gt__, __ge__
to override the corresponding operators.
(I.e., <, <=, ==, !=, >, >=. You gotta love the Fortran heritage.) If a class defines __cmp__ as well,
it is only used when __lt__ etc. have been tried and return NotImplemente
"""

# # 实现方法
# def __lt__(self, other):
#    ...
# def __le__(self, other):
#    ...
# def __gt__(self, other):
#    ...
# def __ge__(self, other):
#    ...
# def __eq__(self, other):
#    ...
# def __ne__(self, other):
#    ...


# Python3中functools中的cmp_to_key函数作为例子

# python3不支持，返回一个高级的比较对象类
def cmp_to_key(mycmp):
    """Convert a cmp= function into a key= function"""
    class K(object):
        __slots__ = ['obj']
        def __init__(self, obj):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        __hash__ = None
    return K

"""
该函数内部定义了一个类，该类有5个方法，分别是__lt__, __gt__，__eq__，__le__，__ge__其实还可以定义__ne__方法。
这分别对应了：小于，大于，等于，小于等于，大于等于，不等于。这六个就是富比较方法。
对象之所以能够比较大小，就是因为这六个富比较方法在其作用。例如，__lt__富比较方法可以直接映射到对应的操作符如“<”,操作更方便简洁。
"""


# 实验python中的富比较方法,__lt__, __gt__, __le__, __ge__, __eq__, __ne__这6个富比较方法


class Test(object):
    def __init__(self, value):
        self.value = value
    def __lt__(self, other):
        print('调用Test的__lt__方法')
        return self.value < other.value
    def __gt__(self, other):
        print('调用Test的__gt__方法')
        return self.value > other.value

t1 = Test(1)
t2 = Test(2)
print(t1 > t2)
print(t2 < t1)
# 当比较两个实例t1和t2的大小时，实际就是调用了对应的富比较方法。
# 例子中时t1 > t2，应该映射到了Test_1类中的__gt__方法，也就是比较了这两个实例的value属性的大小。

# 调用Test的__gt__方法
# False
# 调用Test的__lt__方法
# False

class Test(object):
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        print('调用Test的__lt__方法')
        return self.value < other.value

    def __gt__(self, other):
        print('调用Test的__gt__方法')
        return self.value*10 > other.value   #修改了比较的地方

t1 = Test(1)
t2 = Test(2)
print(t1 > t2)
print(t2 < t1)

# 调用Test的__gt__方法
# True
# 调用Test的__lt__方法
# False


"""

functools，用于高阶函数：指那些作用于函数或者返回其它函数的函数，通常只要是可以被当做函数调用的对象就是这个模块的目标。

在Python 2.7 中具备如下方法，

cmp_to_key，将一个比较函数转换关键字函数；（Python 3 不支持）

partial，针对函数起作用，并且是部分的；

reduce，与python内置的reduce函数功能一样；

total_ordering，在类装饰器中按照缺失顺序，填充方法；

update_wrapper，更新一个包裹（wrapper）函数，使其看起来更像被包裹（wrapped）的函数；

wraps，可用作一个装饰器，简化调用update_wrapper的过程；
"""
