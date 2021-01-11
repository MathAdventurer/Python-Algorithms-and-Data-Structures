#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: Wang,Xudong 220041020 SDS time:2021/1/8

"""
chapter3 基本数据结构

definition of linear structure：
栈、队列、双端队列和列表都是有序的数据集合，其元素的顺序取决于添加顺序或移除顺序。
一旦某个元素被添加进来，它与前后元素的相对位置将保持不变。
这样的数据集合经常被称为线性数据结构 。

线性数据结构可以看作有两端。
这两端有时候被称作“左端”和“右端”，
有时候也被称作“前端”和“后端”。
当然，它们还可以被称作“顶端”和“底端”。

区分线性结构： 真正区分线性数据结构的是元素的添加方式和移除方式，尤其是添加操作和移除操作发生的位置。

"""

'''
3.3 栈
栈:
有时也被称作“下推栈”。它是有序集合添加操作和移除操作总发生在同一端，即“顶端”，另一端则被称为“底端”。
栈中的元素离底端越近，代表其在栈中的时间越长，因此栈的底端具有非常重要的意义。
最新添加的元素将被最先移除。这种排序原则被称作 LIFO (last-in first-out)，即后进先出。
它提供了一种基于在集合中的时间来排序的方式。
最近添加的元素靠近顶端，旧元素则靠近底端。

栈的反转特性：
例如，每一个浏览器都有返回按钮。当我们从一个网页跳转到另一
个网页时，这些网页——实际上是 URL——都被存放在一个栈中。 
当前正在浏览的网页位于栈的顶端，最早浏览的网页则位于底端。 
如果点击返回按钮，便开始反向浏览这些网页。

栈抽象数据类型:
操作顺序：LIFO
Stack() 创建一个空栈。它不需要参数，且会 返回一个空栈。
push(item) 将一个元素添加到栈的顶端。它需要一个参数 item ，且无返回值。
pop() 将栈顶端的元素移除。它不需要参数， 但会返回顶端的元素，并且修改栈的内容。
peek() 返回栈顶端的元素，但是并不移除该元 素。它不需要参数，也不会修改栈的内容。
isEmpty() 检查栈是否为空。它不需要参数， 且会返回一个布尔值。
size() 返回栈中元素的数目。它不需要参数， 且会返回一个整数。


抽象数据类型的实现常被称为数据结构

和其他面向对象编程语言一样，每当需要在 Python 中实现像栈这样的抽象数据类型时，就可以创建新类。
栈 的操作通过方法实现。更进一步地说，因为栈是元素的集合，所以 完全可以利用 Python 提供的强大、简单的原生集合来实现。
这里， 我们将使用列表。

'''
# 使用python实现栈

# 列表的尾部是栈的顶端，直接使用python list的append和pop方法
class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self,item):
        self.items.append(item)
    def pop(self): # 修正空栈，空list问题
        if len(self.items) != 0:
            return self.items.pop()
        else:
            return None
    def peek(self):   # 修正空list，空栈的问题
        if len(self.items) != 0:
            return self.items[len(self.items)-1]
        else:
            return None    # 如果是空栈，peek将返回空值
    def size(self):
            return len(self.items)
    def __str__(self):
        return self.items.__str__()
    def __repr__(self):
        return self.items.__repr__()


# 列表的顶部是栈的顶端，无法直接使用python list的append和pop方法,时间复杂度比较高

class Stack_new:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        # self.items = [item] + self.items  使用insert方法，0是索引
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)

# # 测试 Stack
# s = Stack()
# s.isEmpty()
# s.push(4)
# s.push('dog')
# s.peek()
#
# s.push(True)
# s.size()
# s.isEmpty()
# s.push(8.4)
# s.pop()
# s.pop()
# s.size()
#
# """
# 例子：
# (defun square(n) (* n n))
# """

# 匹配括号以及正确的嵌套关系

from __main__ import Stack

def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:

        symbol = symbolString[index]
        if symbol == '(':   #左括号进栈
           s.push(symbol)
        else:
           if s.isEmpty():
               balanced = False
           else:    # 右括号出栈
               s.pop()      # 此处默认只有两种括号
        index = index + 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

print(parChecker('((((()))'));

# 直接运行和使用print NameError: name 'Ture' is not defined, 此处错误是自己写错了True造成的
# 非常容易出错的typo



# 通用的括号匹配


# 自己写的parchecker函数
def parchecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in '([{':
            s.push(symbol)
        if symbol in ')]}':
            if s.isEmpty():
               balanced = False
            elif '([{'[')]}'.index(symbol)] == s.peek(): #先把判断空放到前面，如果是空的时候，s.peek()会报错
               s.pop()   # 修正Stack类
            else:
               balanced = False
        index = index + 1
    if balanced and s.isEmpty():
        return True
    else:
        return False
print(parchecker('{[(+)]}'));
print(parchecker('({[}])'));

#规范答案, 适用性不好，不能判断一般的含其他运算符的字符串
def parChecker_eg(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
               balanced = False
            else:
               top = s.pop()
               if not matches(top, symbol):
                   balanced = False
        index = index + 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open, close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)
# print(parChecker_eg('{[()]}'));  判断不了'{[(+)]}'
# print(parChecker_eg('({[}])'));


# 下面进行基准测试

import timeit

test_string = '({[(((((((())))))))]}])'

test_1 = timeit.Timer('parChecker_eg(test_string)','from __main__ import parChecker_eg, matches, test_string')

print('The time of parChecker_eg is :',test_1.timeit(number = 100000))

test_2 = timeit.Timer('parchecker(test_string)','from __main__ import parchecker, test_string')

print('The time of parchecker is :',test_2.timeit(number = 100000))



# 将十进制数转换成二进制数
"""
除以进制的算法 基于栈的思想

储存的时候向栈中压入余数是进栈，读取的时候从栈中移除余数


"""


# 用python实现二进制 除以2算法
# 使用内建取余的%运算符

from __main__ import Stack

def divideBy2(decNumber):
    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber = decNumber // 2

    binString = ''
    while not remstack.isEmpty():
        binString =  binString + str(remstack.pop()) #字符串 + 的方法

    return binString

# 扩展对于任意进制的转换

def baseConverter(decNumber,base):
    digits = '0123456789ABCDEF'
    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    newString = ""
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]
    return newString

"""
重要的关于进制
添加一些字母字符到数字中。
例如，十六进制使用 10 个数字以及前 6 个字母来代表 16 位数字。
在代码清单 3-6 中， 为了实现这一方法，第 3 行创建了一个数字字符串来存储对应位置上的数字。
0 在位置 0，1 在位置 1，A 在位置 10，B 在位置 11， 依此类推。
当从栈中移除一个余数时，它可以被用作访问数字的下 标，对应的数字会被添加到结果中。如果从栈中移除的余数是 13， 
那么字母 D 将被添加到结果字符串的最后。
"""


"""
前序、中序和后序表达式

运算符出现在两个操作数的中间 ，所以这种表达式被称作中序表达式

优先级

完全括号表达式：杜绝歧义  


将复杂的中序表达式转换成前序或者后序表达式

后序表达式，运算元素从后往前算
前序表达式，运算元素从前往后计算

(A + B) * C

中序表达式：  (1+4)*3+10/5 eg 中序表达式就是我们日常使用的表达式,由左往右阅读，结构清晰，但需要括号改变优先级，对计算机不友好

前序表达式（波兰表示法Polish notation，或波兰记法）：
一种逻辑、算术和代数表示方法，其特点是操作符置于操作数的前面，如果操作符的元数（arity）是固定的，则语法上不需要括号仍然能被无歧义地解析，
不需要括号来改变优先级，未推广使用。


前序表达式： +AB*C
后序表达式 AB*C+




"""