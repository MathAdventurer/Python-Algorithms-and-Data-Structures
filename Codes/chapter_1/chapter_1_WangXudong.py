#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: Wang,Xudong 220041020 SDS time:2020/11/24

"""
# Python Review
# 1.Data Type
>> > myList = [1, 2, 3, 4]
>> > A = [myList] * 3   #动态引用，注意是【】*3
>> > A
[[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
>> > myList[2] = 45
>> > A

[[1, 2, 45, 4], [1, 2, 45, 4], [1, 2, 45, 4]]
>> >
"""
"""
适用于任何python序列的运算符
索引 []
连接 +
重复 *  重复N进行连接
成员 in 查询元素 返回boolean
长度 len
切片 [:]
int float
boolean: False True
1.1 List
list是序列 可以使用序列运算符
append pop() sort del count #直接修改内容
insert pop(i) reverse (index remove)第一次返回的下标，第一次出现移除
.调用方法并传递值
(54).__add__(21)
range生成代表值序列的范围对象，加入list生成列表，默认0
range(10)
list(range(5,10,2)) #2是步长

1.2 String 
'David'  "" ''
String可以使用序列运算符

center ljust lower find #直接修改内容
count rjust upper split :if没有提供分隔字符，那么 split 方法将会寻找如 制表符、换行符和空格等空白字符。

列表和字符串的主要区别在于，列表能够被修改，字符串则不能。 
列表的这一特性被称为可修改性 。列表具有可修改性，字符串则 不具有。
String object doesn't support item assignment ##不可修改的错误
>>> myName
'David'
>>> myName[0]='X'

string有sorted方法, 没有sort方法：

sorted(iterable, /, *, key=None, reverse=False)
    Return a new list containing all items from the iterable in ascending order.  
    A custom key function can be supplied to customize the sort order, and the
    reverse flag can be set to request the result in descending order.



1.3 tuple 元组
 (, , )
异构数据序列，因此元组 与列表非常相似。
它们的区别 在于，元组和字符串一样是不可修改的。
元组通常写成由括号包含 并且以逗号分隔的一系列值。与序列一样，元组允许之前描述的任一操作。

1.4 set 
无序的
{}
是由零个或多个不可修改的 Python 数据对象组成的无序集合。
集不允许重复元素，并且写成由花括号包含、以逗号分隔的一系列值。
空集由 set() 来表示。
集是异构的，并且可以通过下面的方法赋给变量。(但是必须是immutable的元素组成的)
{False, 4.5, 3, 6, 'cat'}

成员in ( \| 返回一个包含 aset 与 otherset 所有元素的新集) (- 返回一个集，其中包含只出现在 aset 中的元素)
长度len  &交运算  (<=  询问 aset 中的所有元素是否都在 otherset 中 ,直接返回一个boolean)

# Mutable collection of unique unordered immutable objects
  a = {1,2,3,"str",{1,2,3}}
  TypeError: unhashable type: 'set'


1.5 Python 中的collection方法

union intersection difference
issubset  询 问 aset 是 否 为 otherset 的子集
add
remove
pop
clear 清除 aset 中的所有元素 clear() takes no arguments (1 given) 返回空的该类型


1.6 Python 字典
字典是无序结构，由相关的元素对构成，其中每对元素都由一个键和一个值组成。这种键–值对 通常写成键:值的形式。
字典由花括号包含的一系列以逗号分隔的 键–值对表达，如下所示。
{} dict()
dict使用key 而不是 index访问
添加新值 capitals['Utah']='SaltLakeCity'

Utah':'SaltLakeCity' )被放在了字典的第一位， 
第二个添加的键–值对('California':'Sacramento' )则被放在了最后。
键的位置是由散列来决定的，

字典既有运算符，又有方法。
 keys 、values 和 items 方法均会返回包含相应值的对象。
 可以使用 list 函数将字典转换成列表
 
 字典的运算
 索引[] 输入key，返回value
 in 范围boolean key in adict
 del del adict[key] 从字典中删除 key 的键–值对
 
 字典的method
 keys
adict.keys()返回包含字典中所有键的 dict_keys 对象
values
adict.values()返回包含字典中所有值的 dict_values 对象
items
adict.items()返回包含字典中所有键–值对的 dict_items 对象 返回list list中是元组
get
adict.get(k)返回 k 对应的值，如果没有则返回 None
get
adict.get(k, alt)返回 k 对应的值，如果没有则返回 alt
 
 
2.1输入输出
aName = input('Please enter your name: ') input 函数接受一个字符串作为参数。
由于该字符串包含有用的 文本来提示用户输入，因此它经常被称为提示字符串 。
input 函数返回的值是一个字符串，它包含用户 在提示字符串后面输入的所有字符。
如果需要将这个字符串转换成 其他类型，必须明确地提供类型转换。

格式化字符串：
>>> print("Hello")
Hello
>>> print("Hello","World")
Hello World
>>> print("Hello","World", sep="***")
Hello***World
>>> print("Hello","World", end="***")
Hello World***>>>

print(aName, "is", age, "years old.")
print("%s is %d years old." % (aName, age))  % 是字符串运算符， 被称作格式化运算符 。表达式的左边部分是模板(也叫格式化字符串)，
右边部分则是一系列用于格式化字符串的值。需要注意的 是，右边的值的个数与格式化字符串中% 的个数一致。这些值将依次从左到右地被换入格式化字符串。

表 1-9 格式化字符串可用的类型声明
字符
输出格式
d 、i整数
u 无符号整数
f m.dddd 格式的浮点数
e m.dddde+/-xx 格式的浮点数
E m.ddddE+/-xx 格式的浮点数
g 对指数小于-4 或者大于 5 的使用%e ，否则使用%f
c 单个字符
s 字符串，或者任意可以通过 str 函数转换成字符串的 Python 数据对象
% 插入一个常量% 符号

表 1-10 格式化修改符

%20d
将值放在 20 个字符宽的区域中
-
%-20d
将值放在 20 个字符宽的区域中，并且左对齐
+
%+20d
将值放在 20 个字符宽的区域中，并且右对齐
0
%020d
将值放在 20 个字符宽的区域中，并在前面补上 0
.
%20.2f
将值放在 20 个字符宽的区域中，并且保留小数点后 2 位
(name)
%(name)d
从字典中获取 name 键对应的值

3.1控制结构

迭代结构loop
for while
while counter <= 5:
while counter <= 10 and not done:
for item in [1,3,6,2,5]:
分支结构
Python 的缩进模式帮助我们在不需要额外语法元素的情况下有效地关联对应的 if 和 else 。
另一种表达嵌套分支的语法是使用 elif 关键字。将 else 和下 一个 if 结合起来，可以减少额外的嵌套层次。
注意，最后的 else 仍然是必需的，它用来在所有分支条件都不满足的情况下提供默认分支。

使用列表解析式，只需一行代码即可创建完成。可使用迭代和分支结构
sqlist = [x*x for x in range(1,11)]

4 异常处理
逻辑错误会导致诸如除以 0、越界访问列表等非常严重的情况。
这 些逻辑错误会导致运行时错误，进而导致程序终止运行。
通常，这 些运行时错误被称为异常 。



try处理抛出异常

try:
      print(math.sqrt(anumber))
   except:
      print("Bad Value for square root")
      print("Using absolute value instead")
      print(math.sqrt(abs(anumber)))
Bad Value for square root
Using absolute value instead


Traceback类
4.79583152331


raise 语句来触发运行时异常。例如，可以先 检查值是否为负，并在值为负时抛出异常，而不是给 sqrt 函数提 供负数。
下面的代码段显示了创建新的 RuntimeError 异常的结 果。
注意，程序仍然会终止，但是导致其终止的异常是由我们自己 手动创建的。
>>> if anumber < 0:
... raise RuntimeError("You can't use a negative number") ... else:
... print(math.sqrt(anumber))

5. 定义函数
牛顿法求方程的根
先取1/2然后 root= 1/2(root+ (n/root))

6.面向对象
a. Fraction类抽象的分数
所有的类首先都应该有构造方法
在 Python 中，构造方法总是命名为__init__ (即在 init 的前后分别有两个下划线)

b. 继承:逻辑门与电路
继承 使一个类与另一个类相关联，就像人们相互联系一样。孩子从父母那里继承了特征。
与之类似，Python 中的子类可以从父类继承特征数据和行 为。
父类也称为超类。
继承的层次结构:
列表是有序集合的子。因此，我们将列表称为子，有序集合称为父(或者分别称为子类列表和超类序列）

模拟:逻辑门是这个模拟程序的基本构造单元，它们代表其输入和输出之间的布尔代数关系
AND gate
OR gate
NOT gate

python的集合类：1：有序：list str tuple 2：无序：dic set



逻辑门连接 connector类
HAS-A 有一个关系
IS-A 子类与父类的关系




"""
def squareroot(n:int):
    root = n/2
    for k in range(20):
        root = (1/2)*(root + (n/root))
    return root

#print(squareroot(4563))

class Fraction:
    #方法的定义
    #首先创建对象
    def __init__(self,top,bottom):
        self.num = top   #self指向对象本身，形式参数（不需要实际的参数）
        self.den = bottom
        # 分数需要分子与分母两部分状态数据 构造方法中的 self.num 定义了 Fraction 对象有一个叫作num的内部数据对象作为其状态的一部分。同理,
        # self.den 定义了分母。
        # 创建对象的时候能够知道初始值
    #打印对象的两种方法
    # 定义show方法
    def show(self):   #self只是一个形式参数
        print(self.num,"/",self.den)  #为什么有间距？？
    # 重写 方法 定义一个名为__str__ 的方法
    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    # 定义加法  \为续行符
    # def __add__(self, otherfraction):
    #     newnum = self.num * otherfraction.den + \
    #              self.den * otherfraction.num
    #     newden = self.den * otherfraction.den
        return Fraction(newnum,newden)
    # 化简分数的方法 greatest common divisor，GCD
    # 欧几里得算法 化简分数 不用loop用判断写不出来
    def gcd(m:int,n:int):
        if n != 0 and m != 0:
            while m%n != 0:
                oldm = m
                oldn = n
                m = oldn
                n = oldm%oldn
            return n
        else:
            return None
    def __add__(self,otherfraction):
        newnum = self.num * otherfraction.den + \
                 self.den * otherfraction.num
        newden = self.den * otherfraction.den
        common = Fraction.gcd(newnum,newden)   #如果函数定义在class内部，调用的时候需要用class.method,定义在外部可以直接调用gcd
        return Fraction(newnum//common,newden//common) #只取了余数

    # 浅相等与真相等
    # 浅相等：同一个对象的引用(根据引用来判断)才为真,在当前实现中，分子和分母相同的两个不同的对象是不相等的。
    # 深相等：根据值来判断相等，而不是根据引用
    def __eq__(self,other):
        firstnum = self.num * other.den
        secondnum = self.den * other.num
        return firstnum == secondnum

    def __le__(self, other):
        firstnum = self.num * other.den
        secondnum = self.den * other.num
        return firstnum <= secondnum


myf = Fraction(3,5)
print(myf)
myf.show()
print(myf.__str__())
f1 = Fraction(1,4)
f2 = Fraction(1,2)
f3 = Fraction(2,8)
# f1+f2
print('\n')
print(f1+f2)
print(f2.__eq__(f3))
print(f1 == f3)
print(f2.__le__(f3))
print(f2 <= f3)
print(f1 <= f3)
print(f1.__le__(f3))
print(f1 >= f3)

#{TypeError: unsupported operand type(s) for +:'instance' and 'instance'}#
#Fraction 对象 myf 并不知道如何响应打印请求。print 函数 要求对象将自己转换成一个可以被写到输出端的字符串。
# <__main__.Fraction object at 0x10fb431f0> myf 唯 一能做的就是显示存储在变量中的实际引用(地址本身)
# IS-A 关系子类与父类
class LogicGate:
    def __init__(self,n):
        self.label = n
        self.output = None
    def getLabel(self):
        return self.label
    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output
    # pin引脚的概念,输入

class BinaryGate(LogicGate):
    def __init__(self,n):
        super().__init__(n)
        self.pinA = None
        self.pinB = None
    def getPinA(self):
        return int(input("Enter Pin A input for gate " + self.getLabel() + "-->"))
    def getPinB(self):
        return int(input("Enter Pin B input for gate " + self.getLabel() + "-->"))

class UnaryGate(LogicGate):
   def __init__(self, n):
       super().__init__(n)
       self.pin = None
   def getPin(self):
       return int(input("Enter Pin input for gate " + self.getLabel() + "-->"))


class AndGate(BinaryGate):

    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 1 and b == 1:
            return 1
        else:
            return 0

class OrGate(BinaryGate):

    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 1 or b == 1:
            return 1
        else:
            return 0
class NotGate(UnaryGate):

    def __init__(self,n):
        super().__init__(n)

    def performGateLogic(self):
        pin = self.getPin()
        if pin == 1 :
            return 0
        else:
            return 1

# Connector  HAS-A 关系 (HAS-A 意即“有一个”)
# Connector 类并不在逻辑门的继承层次结构中。但是，它会使用该结构，从而使每一个连接器的两端都有一个逻辑门
class Connector:
    def __init__(self,fgate,tgate):
        self.fgate = fgate
        self.tgate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate

    #setNextPin method

    def setNextPin(self,source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB == source
            else:
                raise RuntimeError('Error: NO EMPTY PINS')

    def getPinA(self):
        if self.pinA == None:
            return input('Enter Pin A input for gate' + \
                         self.getName()+"-->")
        else:
            return self.pinA.getFrom().getOutput()

# 如果 a 有 __add__ 方法， 而且返回值不是 NotImplemented， 调用a.__add__(b)， 然后返回结果。
# 如果 a 没有 __add__ 方法， 或者调用 __add__ 方法返回NotImplemented， 检查 b 有没有 __radd__ 方法， 如果有， 而且没有返回 NotImplemented， 调用 b.__radd__(a)， 然后返回结果。
# 如果 b 没有 __radd__ 方法， 或者调用 __radd__ 方法返回NotImplemented， 抛出 TypeError， 并在错误消息中指明操作数类型不支持。

if __name__ == "__main__":

    g1 = AndGate("G1")
    #g1.getOutput()
    print(g1.getOutput()) #print会直接调用
    g2 = OrGate("G2")
    print(g2.getOutput())
    g3 = NotGate("G3")
    print(g3.getOutput())
    g1 = AndGate("G1")
    g2 = AndGate("G2")
    g3 = OrGate("G3")
    g4 = NotGate("G4")
    c1 = Connector(g1,g3)
    c2 = Connector(g2,g3)
    #c3 = Connector(g3,g4)



myf = Fraction(3,5)
print(myf)
myf.show()
print(myf.__str__())
f1 = Fraction(1,4)
f2 = Fraction(1,2)
f3 = Fraction(2,8)
# f1+f2
print('\n')
print(f1+f2)
print(f2.__eq__(f3))
print(f1 == f3)
print(f2.__le__(f3))
print(f2 <= f3)
print(f1 <= f3)
print(f1.__le__(f3))
print(f1 >= f3)



