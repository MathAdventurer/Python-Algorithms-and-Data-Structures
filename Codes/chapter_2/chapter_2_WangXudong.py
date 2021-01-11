#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: Wang,Xudong 220041020 SDS time:2020/12/1
"""
程序与算法不同
算法的可读性与精简

算法分析关心的是基于所使用的计算资源比较算法
一 是考虑算法在解决问题时要占用的空间或内存。
另一种思考方式是根据算法执行所需的时间进行分析和比较。这个
指标有时称作算法的执行时间 或运行时间
基准分析
time函数  time.time()以秒为单位返回自指定时间点起到当前的系统时钟时间


大O记法
问题规模
数量级函数描述的就是，当  增长时，  增长最快的部分。数量级 （order of magnitude）常被称作大
 记法 （  指order），记作  。它提供了步骤数的一个有用的近似方法。
 函数为  函数中起决定性作用的部分提供了简单的表示。

 算法的性能有时不仅依赖于问题规模，还依赖于数据值。对于这种算法，要用最坏情况 、最好情况 和普通情况
 来描述性能。最坏情况指的是某一个数据集会让算法的性能极差；另一个数据集可能会让同一个算法的性能极好（最好情况）。
 大部分情况下，算法的性能介于两个极端之间（普通情况）。
"""
import time


# 计算前m个数的和


def sumOfN(n):
    theSum = 0
    for i in range(1, n + 1):
        theSum = theSum + i

    return theSum


def sumOfN2(n):
    start = time.time()

    theSum = 0
    for i in range(1, n + 1):
        theSum = theSum + i

    end = time.time()

    return theSum, end - start


def sumOfN3(n):
    start = time.time()
    end = time.time()

    return (n * (n + 1)) / 2, end - start



## 查找异序词
# 清点法


#先取字符串1中的一个字符，开始寻找第二个字符串中的是否存在，存在，将此处的字符串消除掉,
# 找到一次就停止，比如hello 和 heoll中两个l，每次每个l一遇到就跳出这次while，如果不存在，返回false

def anagramSolution(s1, s2):
    start = time.time()
    alist = list(s2)  #字符串是不可修改的，先进行转换

    pos1 = 0   #初始的比较位置
    stillOK = True #返回值

    while pos1 < len(s1) and stillOK:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:  #这里面的not found保证了每次遇到相同的就跳出这次循环
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1
        if found:
            alist[pos2] = None
        else:
            stillOK = False
        pos1 = pos1 + 1
    end = time.time()
    return stillOK, end-start
# algorithm analysis
# 算法的复杂度相当于遍历了1到n的和，因为每次字符串2的长度在匹配之后都会降低一
# 时间的复杂度是n -square


# 排序法

def anagramSolution2(s1, s2):
    start = time.time()
    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()

    pos = 0

    matches = True

    while pos < len(s1) and matches:
        if alist1[pos] == alist2[pos]:
            pos = pos + 1
        else:
            matches = False
    end = time.time()
    return matches, end-start

# 时间复杂度是n方或者nlogn 主要时间消耗在sort方法上

# 暴力穷举法
# 第一个字符串有n个字符的时候，生成n！个字符串


# 计数法
# 异序词肯定含有相同的字符个数 有缺陷，不能检测非字母的字符
# 尝试改进，使用两个几何元素的list的unique的并数量
# 线性的时间复杂度，但是占用的空间来进行计数，用算法的空间换了时间

def anagramSolution4(s1, s2):
    start = time.time()
    c1 = [0] * 100
    c2 = [0] * 100
# ord(c, /)  Return the Unicode code point for a one-character string.
    for i in range(len(s1)):    # 2n的算法复杂度
        pos = ord(s1[i]) - ord('0')
        c1[pos] = c1[pos] + 1

    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('0')
        c2[pos] = c2[pos] + 1

    j = 0
    stillOK = True
    while j < 100 and stillOK:  #可能的算法复杂度100，这里如果只比较字母的话，可能会循环100次
        if c1[j] == c2[j]:
            j = j + 1
        else:
            stillOK = False
    end = time.time()
    return stillOK, end - start



## 最初版的测试算法复杂度
# if __name__ == '__main__':
#     print(sumOfN(5))
#
#     for i in range(5):
#         print('Sum is %d required %10.7f seconds' % sumOfN2(10000))
#     print('\n')
#     for i in range(5):
#         print('Sum is %d required %10.7f seconds' % sumOfN3(10000))

# # 对于查找异序词的算法复杂度分析
# if __name__ == "__main__":
#     # print('清点法')
#     # for i in range(10):
#     #     print('The outcome is %s and uses %10.7f seconds'%anagramSolution('hello','heoll'))
#     # print('排序法')
#     # for i in range(10):
#     #     print('The outcome is %s and uses %10.7f seconds' % anagramSolution2('hello', 'heoll'))
#     print('清点法')
#     for i in range(10):
#         print('The outcome is %s and uses %10.7f seconds' % anagramSolution('/Users/mac/opt/anaconda3/bin/python/Applications/PyCharm.app/Contents/plugins/python/helpers/', '/Users/mac/opt/anaconda3/bin/python/Applications//pythonPyCharm.app/Contents/plugins/helpers/'))
#     print('排序法') #增加字符串的长度，时间更加明显，使用排序法的nlogn的算法时间更短
#     for i in range(10):
#         print('The outcome is %s and uses %10.7f seconds' % anagramSolution2('/Users/mac/opt/anaconda3/bin/python/Applications/PyCharm.app/Contents/plugins/python/helpers/', '/Users/mac/opt/anaconda3/bin/python/Applications//pythonPyCharm.app/Contents/plugins/helpers/'))
#     print('计数法')
#     for i in range(10):
#         print('The outcome is %s and uses %10.7f seconds' % anagramSolution4(
#             '/Users/mac/opt/anaconda3/bin/python/Applications/PyCharm.app/Contents/plugins/python/helpers/',
#             '/Users/mac/opt/anaconda3/bin/python/Applications//pythonPyCharm.app/Contents/plugins/helpers/'))



"""

python 数据结构的性能
1. 列表
索引和赋值，与列表的长度无关，操作的复杂度是常数阶的
加长列表 追加执行操作连接，常数阶的复杂度，k长度 O(k)
"""
# 从0开始生成含n个数的列表
def test1():
    l = []
    for i in range(1000):
        l = l + [i]

def test2():
    l = []
    for i in range(1000):
        l.append(i)

def test3():
    l = [i for i in range(1000)]

def test4():
    l = list(range(1000))

# 进行时间的测试
# 进行格式化输出，使用time.time()，与函数返回值
# print(time.time())
# test1()
# print(time.time())
# test2()
# print(time.time())
# test3()
# print(time.time())
# test4()
# print(time.time())

# 使用 timeit 模块
"""
首先创建一个 Timer 对象，其参数是两条 Python 语句。第 1 个参数是要为之计时的 Python 语句;第 2 个参
数是建立测试的语句。timeit 模块会统计多次执行语句要用多久。 
默认情况下，timeit 会执行 100 万次语句，并在完成后返回一 个浮点数格式的秒数。
不过，既然这是执行 100 万次所用的秒数， 就可以把结果视作执行 1 次所用的微秒数。
"""
# from threading import Timer
# from timeit import Timer
# if __name__ == '__main__':
#     t1 = Timer('test1()', 'from __main__ import test1');
#     print('concat', t1.timeit(number = 1000),'milliseconds')
#
#     t2 = Timer('test2()', 'from __main__ import test2');
#     print('append', t2.timeit(number = 1000),'milliseconds')
#
#     t3 = Timer('test3()', 'from __main__ import test3');
#     print('comprehension', t3.timeit(number = 1000),'milliseconds')
#
#     t4 = Timer('test4()', 'from __main__ import test4');
#     print('list range', t4.timeit(number = 1000),'milliseconds')

"""
from __main__ import test1 将 test1 函数从__main__ 命名空间导入到 timeit 设置计时的命
名空间。timeit 模块这么做，是为了在一个干净的环境中运行计
时测试，以免某些变量以某种意外的方式干扰函数的性能。
"""

# 此处调用函数的开销没有计算进去，假设调用函数的时间是相同的，可以调用空函数然后后面减去
# 在列表末尾调用 pop 时，操作是常数阶的，在列表头一个元素或中间 某处调用 pop 时，则是n阶的。

# pop的性能分析

# from timeit import Timer
# popzero = Timer('x.pop(0)','from __main__ import x');
# popend = Timer('x.pop()','from __main__ import x');
#
# x = list(range(2000000));
# print(popzero.timeit(number = 1000));
# x = list(range(2000000));
# print(popend.timeit(number= 1000));
# # 比较pop(0) 和 pop() 在不同列表长度下的性能
# popzero=Timer("x.pop(0)", "from __main__ import x")
# popend=Timer("x.pop()", "from __main__ import x")
# print("pop(0) pop()")
# for i in range(1000000,100000001,1000000): #测试100次
#     x = list(range(i))
#     pt = popend.timeit(number=1000)
#     x = list(range(i))
#     pz = popzero.timeit(number=1000)
#     print("%15.5f, %15.5f" % (pz, pt))

"""
2.3.2 字典
字典的取值赋值，检验包含都是常数阶的
某些特殊情况下，包含、取值、赋值等操作的时间复杂度可能变成 O(n)
复制 O(n) 删除 O(1) 遍历 O(n)
"""
# 比较列表和字典的包含操作 list的包含操作是n，字典是常数阶的

import timeit
import random

# random.randrange(10) 在0到9之间随机生成一个数值
# 'random.randrange(%d) in x'%i 判断使用range(i) 生成的list中包不包含使用随机数取出来的数值

for i in range(10000,1000001,20000):
    t = timeit.Timer('random.randrange(%d) in x'%i, 'from __main__ import random,x')
    x = list(range(i))
    lst_time = t.timeit(number=1000)
    x = {j:None for j in range(i)} # 字典比较是取键
    d_time = t.timeit(number=1000)
    print('%d,%10.3f,%10.3f'%(i,lst_time,d_time))

"""
10000,     0.087,     0.001
30000,     0.265,     0.001
50000,     0.417,     0.001
70000,     0.590,     0.001
90000,     0.756,     0.001
110000,     0.933,     0.001
130000,     1.245,     0.001
150000,     1.241,     0.001
170000,     1.467,     0.001
190000,     1.624,     0.001
210000,     1.764,     0.001
230000,     1.911,     0.001
250000,     2.046,     0.001
270000,     2.369,     0.001
290000,     2.562,     0.001
310000,     2.095,     0.001
330000,     1.613,     0.001
350000,     1.696,     0.001
370000,     1.725,     0.001
390000,     1.998,     0.001
410000,     1.965,     0.001
430000,     1.987,     0.001
450000,     2.071,     0.001
470000,     2.238,     0.001
490000,     2.319,     0.001
510000,     2.367,     0.001
530000,     2.591,     0.001
550000,     2.781,     0.001
570000,     2.683,     0.001
590000,     2.966,     0.001
610000,     2.758,     0.001
630000,     3.280,     0.001
650000,     3.049,     0.001
670000,     3.135,     0.001
690000,     3.307,     0.001
710000,     3.228,     0.001
730000,     3.442,     0.001
750000,     4.015,     0.001
770000,     3.755,     0.001
790000,     3.596,     0.001
810000,     3.732,     0.001
830000,     3.857,     0.001
850000,     3.978,     0.001
870000,     4.109,     0.001
890000,     3.981,     0.001
910000,     4.292,     0.001
930000,     4.389,     0.001
950000,     5.248,     0.001
970000,     5.088,     0.001
990000,     4.837,     0.001
"""

"""
时间复杂度网站
https://wiki.python.org/moin/TimeComplexity
"""