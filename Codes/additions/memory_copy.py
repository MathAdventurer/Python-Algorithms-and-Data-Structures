#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: Wang,Xudong 220041020 SDS time:2021/1/24

# Python 中变量在内存的存储与地址变化详解(深浅拷贝，值/引用传递、可变不可变数据类型)

"""
1.
Python的变量保存是值的引用，变量是内存及其地址的抽象

Python中一切变量都是对象,变量的存储采用了引用语义的方式, 存储的只是一个变量的值所在的内存地址，而不是这个变量的值本身
变量所需的存储空间大小一致，因为变量只是保存了一个引用。也被称为对象语义和指针语义。
变量的每一次初始化，都开辟了一个新的空间，将新内容的地址赋值给变量

2.
值语义：有些语言采用的不是这种方式，它们把变量的值直接保存在变量的存储区里，这种方式被我们称为值语义，
例如C语言，采用这种存储方式，每一个变量在内存中所占的空间就要根据变量实际的大小而定，比如 c中 int 一般为2个字节 而char为一个字节

3.
- id函数

id函数：你可以通过python的内置函数 id() 来查看对象的身份(identity)，这个所谓的身份其实就是 对象 的内存地址
就是获取对象在内存中的地址

- 通过内存地址访问变量
import ctypes
value = 'hello world'  # 定义一个字符串变量
address = id(value)  # 获取value的地址，赋给address
get_value = ctypes.cast(address, ctypes.py_object).value  # 读取地址中的变量
print(get_value)

- 对于变量的赋值
我们把不同的值赋给变量时候，变量指向的地址发生变化，但是相同的值地址不发生变化。
对于变量进行赋值时，每一次的赋值都会产生一个新的空间地址，将新内容的地址赋值给变量

- 复杂的数据类型，列表，元组，字典等修改与赋值
对于这些复杂数据类型，如果修改其中某一项元素的值，或者添加几个元素，不会改变其本身的地址，只会改变其内部元素的地址引用，
但是如果对其进行重新赋值操作时，就会给列表重新赋予一个地址，来覆盖之前的地址这时列表地址会发生改变


"""
import ctypes
list1 = [1,2,3,4,5]
print(id(list1))
print(type(ctypes.cast(id(list1),ctypes.py_object))) # <class 'ctypes.py_object'>
print(ctypes.cast(id(list1),ctypes.py_object)) # py_object([1, 2, 3, 4, 5])
print(ctypes.cast(id(list1),ctypes.py_object).value) # [1, 2, 3, 4, 5]

list1.append("a")
print(id(list1))
temp_address = id(list1)
list1 = [1,2,4,5] # 初始化（赋值）之后，地址发生改变
print(id(list1))
list2 = ctypes.cast(temp_address,ctypes.py_object).value # 内存并没有被释放
print(id(list2))

"""
4. 
引用复制“=”进行复制
分片复制[:]进行复制
修改list1之后list2跟list1相同，但是list3却没发生变化
在我们创建list1的时候，Python已经了开辟list1的地址，并且分别指向了其中的值，而我们用“=”进行复制时，
只是会给现存的对象添加一个新的引用，并不会在内存中生成新的对象
copy()函数和分片相同

list1 = [1,2,3]
print(id(list1))
list2 = list1 # list1和list2指向的是同一个地址, 多了一个指向该列表地址的引用
print(id(list2))
list3 = list1[:] # 分片[:]复制是不同的，会创建一个新的对象
print(id(list3))
list1.append(4)
print(id(list1))
print(list2)
print(id(list2))
print(list3)

"""

"""
5. 
Python支持相同的值的不同对象，相当于内存中对于同值的对象保存了多份
但是上面只是对于可变数据类型适用，对于不可变数据类型，内存中只能有一个相同值的对象
当然，具体也要看有没有产生新的对象，如果产生新的对象，则改变的那个列表会指向新的地址

"""

def func(val1):
    print('val1: {}, id: {}'.format(val1, id(val1)))  # val1: [1, 2, 3], id: 43499976
    val2 = val1
    print('val2: {}, id: {}'.format(val2, id(val2)))  # val2: [1, 2, 3], id: 43499976
    val2.append(4)
    print('val2: {}, id: {}'.format(val2, id(val2)))  # val2: [1, 2, 3, 4], id: 43499976
    val2 = val2 + [5] #产生了新的对象
    print('val2: {}, id: {}'.format(val2, id(val2)))  # val2: [1, 2, 3, 4, 5], id: 43500296


a = [1, 2, 3]
print('a: {}, id: {}'.format(a, id(a)))  # a: [1, 2, 3], id: 43499976
func(a)
print('a: {}, id: {}'.format(a, id(a)))  # a: [1, 2, 3, 4], id: 43499976


"""
6. 
可变数据类型于不可变数据类型: 内存中的内容（值）是否可以被改变
可变数据类型：列表list和字典dict,集合set
不可变数据类型：整型int、浮点型float、字符串型string和元组tuple

（1）不可变数据类型，不允许变量的值发生变化，如果改变了变量的值，相当于是新建了一个对象，而对于相同的值的对象，
在内存中则只有一个对象，就是不可变数据类型引用的地址的值不可改变

（2）可变数据类型，允许变量的值发生变化，即如果对变量进行append、+=等这种操作后，
只是改变了变量的值，而不会新建一个对象，变量引用的对象的地址不会改变，只是对应地址的内容改变或者地址发生了扩充，
所以对于相同的值的不同对象，会存在多份，即每个对象都有自己的地址(首地址在变量值改变后并不会改变，但是地址发生了扩充)

"""

""" 
7. 
浅拷贝和深拷贝
copy.copy() 浅拷贝；
copy.deepcopy() 深拷贝

1.浅拷贝：不管多么复杂的数据结构，浅拷贝都只会copy一层。原子对象元素的引用

深拷贝:深拷贝会完全复制原变量相关的所有数据,直到最后一层，在内存中生成一套完全一样的内容,
在这个过程中我们对这两个变量中的一个进行任意修改都不会影响其他变量

浅拷贝 只拷贝父对象(一层)，不会拷贝对象的内部的可变子对象(多层)。
浅拷贝是指拷贝的只是原子对象元素的引用，换句话说，浅拷贝产生的对象(k1,k2,k3) 本身是新的，但是它的内容不是新的，只是对原子对象的一个引用。

2. 深拷贝就是在内存中重新开辟一块空间，不管数据结构多么复杂，只要遇到可能发生改变的数据类型，就重新开辟一块内存空间把内容复制下来，直到最后一层。

3. 引用复制（赋值拷贝）
“=”多了几个变量指向同一个地址

使用切片[:]操作
使用工厂函数（如list/dir/set）
使用copy模块中的copy()函数

"""

import copy
list1=[1,2,3]
list2=[4,5,list1]
list2
list3 = list2.copy()  #list3浅拷贝
list4 = copy.deepcopy(list2)  #list4深拷贝

list1 = [6,6,6]
list2
list3
list4


"""
8.
引用传递与值传递：
可变对象为引用传递，不可变对象为值传递。（函数传值）

1，值传递： 简单来说 对于函数输入的参数对象，函数执行中首先生成对象的一个副本，并在执行过程中对副本进行操作。执行结束后对象不发生改变
即在堆栈中开辟了内存空间以存放由主调函数放进来的实参的值，从而成为了实参的一个副本。
值传递的特点是被调函数对形式参数的任何操作都是作为局部变量进行，不会影响主调函数的实参变量的值。（被调函数新开辟内存空间存放的是实参的副本值）

2. 引用传递：当传递列表或者字典时，如果改变引用的值，就修改了原始的对象。（被调函数新开辟内存空间存放的是实参的地址）

"""

# 值传递不会改变原来函数的值

def Change(b):
    b += 2   #传递进来的为不可变对象，为值传递  相当于相同值的一个副本
    print(id(b))
    print (b)
    return

a = 2
print(id(a))
Change(a)
print (a)
print(id(a))

# 4403210624 a
# 4403210688 b
# 4 function output
# 2 a
# 4403210624 a's address

# 引用传递
def Change(str1):
    str1[1] ="changed " # 此处修改就是直接修改string的值
    return

string = ['hello world',2,3]
print (string)
Change(string)
print (string)

# ['hello world', 2, 3]
# ['hello world', 'changed ', 3]


"""
9. 
在函数调用中无法直接修改整个列表或字典的值 如果这样做，就是相当于也是相当于创建副本的值传递 !!!
"""
def Change(str1):
    str1 =[6,7]   # 直接修改整个列表，也是相当于创建副本的值传递
    return

string = ['hello world',2,3]
print (string)
Change(string) # 此处产生的是值传递
print (string)

# ['hello world', 2, 3]
# ['hello world', 2, 3]


# # 装饰器未能实现深拷贝
# from functools import wraps
# import copy
# a = [1,2,43,5]
# def decorator(func):
#     @wraps(func)
#     def wrapper():
#         print("Re define the copy to deep copy")
#         a.copy  = copy.deepcopy
#     return wrapper
# @decorator
# a.copy()
# print(a.copy())
#
# # 创建子类实现深拷贝属性
#
# class list_new(list):
#     def __init__(self):
#         super().__init__()
#     def deepcopy(self):
#         return copy.deepcopy(self)

