#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: Wang,Xudong 220041020 SDS time:2021/1/19


"""
金融科技，交易所开发，Python高级工程师：
根据业务需求涉及前端的开发，区块链钱包，交易所行情，涉及python rust.

- 装饰器：面向切片的编程，主要作用，面向切片编程
- 语法糖



"""
# 装饰器

"""
装饰器(Decorators)是 Python 的一个重要部分。简单地说：他们是修改其他函数的功能的函数。
他们有助于让我们的代码更简短，也更Pythonic（Python范儿）。

"""
def decorarot(fn):
    context = 1
    def wrapper(*args,**kwargs):
        print("context",context)
        return fn(*args,**kwargs)
        print("after context output", context) # 不会被执行
    return wrapper
@decorarot
def func():
    print("I am the target")

if __name__ =="__main__":
    func()


# 一切皆对象

def hi(name = "hello world!"):
    return name
print(hi())

greet = hi

print(greet())

del hi
print(hi())

print(greet())


# 在函数中定义函数

def hi(name="yasoob"):
    print("now you are inside the hi() function")

    def greet():
        return "now you are in the greet() function"

    def welcome():
        return "now you are in the welcome() function"

    print(greet())
    print(welcome())
    print("now you are back in the hi() function")


hi()

# output:now you are inside the hi() function
#       now you are in the greet() function
#       now you are in the welcome() function
#       now you are back in the hi() function

# 上面展示了无论何时你调用hi(), greet()和welcome()将会同时被调用。
# 然后greet()和welcome()函数在hi()函数之外是不能访问的，比如：

welcome()
# outputs: NameError: name 'welcome' is not defined




# 从函数中返回函数
def hi(name="yasoob"):
    def greet():
        return "now you are in the greet() function"

    def welcome():
        return "now you are in the welcome() function"

    if name == "yasoob":
        return greet
    else:
        return welcome


a = hi() #a相当于赋值了greet这个函数，greet函数是没有参数输入的
print(a)
# outputs: <function greet at 0x7f2143c01500>

# 上面清晰地展示了`a`现在指向到hi()函数中的greet()函数
# 现在试试这个

print(a())

print(a(name ='hello'))#会报错

print(hi(name = "hello"))
print(hi(name = "hello")())

a = hi(name = "hello")
print(a(name ='hello'))
# outputs: now you are in the greet() function
"""
再次看看这个代码。在 if/else 语句中我们返回 greet 和 welcome，而不是 greet() 和 welcome()。为什么那样？
这是因为当你把一对小括号放在后面，这个函数就会执行；然而如果你不放括号在它后面，那它可以被到处传递，并且可以赋值给别的变量而不去执行它。 
你明白了吗？让我再稍微多解释点细节。
当我们写下 a = hi()，hi() 会被执行，而由于 name 参数默认是 yasoob，所以函数 greet 被返回了。如果我们把语句改为 a = hi(name = "ali")，
那么 welcome 函数将被返回。我们还可以打印出 hi()()，这会输出 now you are in the greet() function。

"""


# 将函数作为参数传给另一个函数

def hi():
    return "hi yasoob!"


def doSomethingBeforeHi(func):
    print("I am doing some boring work before executing hi()")
    print(func()) # 执行输入的函数


doSomethingBeforeHi(hi) # 函数hi作为一个参数输入
# outputs:I am doing some boring work before executing hi()
#        hi yasoob!

# 开始装饰器

def a_new_decorator(a_func):
    def wrapTheFunction():
        print("These are some precedures executed before executing a_func()")
        a_func()
        print("These are some precedures executed after executing a_func()")
    return wrapTheFunction
"""
  上面缩进层次不对的时候
  File "<ipython-input-30-98e9f7308003>", line 1, in <module>
    a_function_requiring_decoration()
TypeError: 'NoneType' object is not callable
"""
def a_function_requiring_decoration():
    print("This is the function which needs to be decorated")

a_function_requiring_decoration()
# 对函数进行装饰
a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)

a_new_decorator(a_function_requiring_decoration)()

a_function_requiring_decoration()

print(a_function_requiring_decoration)  # <function a_new_decorator.<locals>.wrapTheFunction at 0x7fdc9044f940>

# @函数，@使用简短的方式来生成一个被装饰的函数

# @a_new_decorator（接受一个函数作为输入）后面跟需要进行装饰的函数，再直接执行后面需要装饰的函数，就完成的装饰
# 等同于 a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
@a_new_decorator

def a_function_requiring_decoration():
    """Hey you! Decorate me!"""
    print("I am the function which needs some decoration to "
          "remove my foul smell")

a_function_requiring_decoration()
print(a_function_requiring_decoration.__name__) # wrapTheFunction

"""
Ouput输出应该是"a_function_requiring_decoration"。这里的函数被warpTheFunction替代了。
它重写了我们函数的名字和注释文档(docstring)。幸运的是Python提供给我们一个简单的函数来解决这个问题，那就是functools.wraps。
我们修改上一个例子来使用functools.wraps：
"""




from functools import wraps

def a_new_decorator(a_func):
    @wraps(a_func)
    def wrapTheFunction():
        print('执行之前')
        a_func()
        print('执行之后')
    return wrapTheFunction  # 返回的是一个函数

@a_new_decorator
# a_new_decorator = a_new_decorator(a_new_decorator)
def testdecorator():
    print("hello world, this is a output used to test the decorator!")

testdecorator()
print(testdecorator.__name__) #testdecorator


"""

*args :就是所有参数的数组 

**kwargs : 当传入key=value时存储的字典

def test(a,*args,**kwargs):
    print a
    #print b
    #print c
    print args
    print kwargs
 
test(1,2,3,d='4',e=5)
输出结果：
1
(2, 3)
{'e': 5, 'd': '4'}
 
意思就是1还是参数a的值，args表示剩余的值，kwargs在args之后表示成对键值对。
 
 def foo(*args, **kwargs):
    print 'args = ', args
    print 'kwargs = ', kwargs
    print '---------------------------------------'
 
if __name__ == '__main__':
    foo(1,2,3,4)
    foo(a=1,b=2,c=3)
    foo(1,2,3,4, a=1,b=2,c=3)
    foo('a', 1, None, a=1, b='2', c=3)
输出结果如下：
args =  (1, 2, 3, 4) 
kwargs =  {} 
--------------------------------------- 
args =  () 
kwargs =  {'a': 1, 'c': 3, 'b': 2} 
--------------------------------------- 
args =  (1, 2, 3, 4) 
kwargs =  {'a': 1, 'c': 3, 'b': 2} 
--------------------------------------- 
args =  ('a', 1, None) 
kwargs =  {'a': 1, 'c': 3, 'b': '2'} 
---------------------------------------
 
可以看到，这两个是python中的可变参数。*args表示任何多个无名参数，它是一个tuple；
**kwargs表示关键字参数，它是一个dict。
并且同时使用*args和**kwargs时，必须*args参数列要在**kwargs前，像foo(a=1, b='2', c=3, a', 1, None, )
这样调用的话，会提示语法错误“SyntaxError: non-keyword arg after keyword arg”。
 
 
 
*args 返回的是一个tuple

**kwargs还有一个很漂亮的用法，就是创建字典：
 
    def kw_dict(**kwargs):
        return kwargs
    print kw_dict(a=1,b=2,c=3) == {'a':1, 'b':2, 'c':3}
其实python中就带有dict类，使用dict(a=1,b=2,c=3)即可创建一个字典了。

"""

def create_tuple(*args):
    return args
print(create_tuple(1,2,43,_,444))
# str(_) Out[7]: ''

# 装饰器的蓝本规范

from functools import wraps

def decorator_name(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        if not can_run:
            return "Function will not run"
        return f(*args,**kwargs)
    return decorated
@a_new_decorator
@decorator_name
def func():
    return("Function is running")

can_run = True
print(func())

can_run = False
print(func())


## 装饰器使用场景

from functools import wraps

# 授权(Authorization)
# 装饰器能有助于检查某个人是否被授权去使用一个web应用的端点(endpoint)。它们被大量使用于Flask和Django web框架中。
# 这里是一个例子来使用基于装饰器的授权：
def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            authenticate()
        return f(*args, **kwargs)

    return decorated

# 授权(Authorization)
# 装饰器能有助于检查某个人是否被授权去使用一个web应用的端点(endpoint)。它们被大量使用于Flask和Django web框架中。
# 这里是一个例子来使用基于装饰器的授权：

# 日志(Logging)
from functools import wraps


def logit(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)

    return with_logging


@logit
def addition_func(x):
    """Do some math."""
    return x + x


result = addition_func(4)
# Output: addition_func was called


"""
带参数的装饰器
"""

from functools import wraps

def logit(logfile='out.log'):
    def logging_decorator(func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)
            # 打开logfile，并写入内容
            with open(logfile, 'a') as opened_file:
                # 现在将日志打到指定的logfile
                opened_file.write(log_string + '\n')
            return func(*args, **kwargs)

        return wrapped_function

    return logging_decorator

@logit()
def myfunc1():
    pass
myfunc1()

# Output: myfunc1 was called
# 现在一个叫做 out.log 的文件出现了，里面的内容就是上面的字符串

@logit(logfile='func2.log')
def myfunc2():
    pass
myfunc2()
# Output: myfunc2 was called
# 现在一个叫做 func2.log 的文件出现了，里面的内容就是上面的字符串

"""
装饰器类
现在我们有了能用于正式环境的logit装饰器，但当我们的应用的某些部分还比较脆弱时，异常也许是需要更紧急关注的事情。
比方说有时你只想打日志到一个文件。而有时你想把引起你注意的问题发送到一个email，同时也保留日志，留个记录。
这是一个使用继承的场景，但目前为止我们只看到过用来构建装饰器的函数。
幸运的是，类也可以用来构建装饰器。那我们现在以一个类而不是一个函数的方式，来重新构建logit。
"""

from functools import wraps


class logit(object):
    def __init__(self, logfile='out.log'):
        self.logfile = logfile

    def __call__(self, func):
        @wraps(func)  #相当于一个装饰器
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)
            # 打开logfile并写入
            with open(self.logfile, 'a') as opened_file:  #语法糖
                # 现在将日志打到指定的文件
                opened_file.write(log_string + '\n')
            # 现在，发送一个通知
            self.notify()
            return func(*args, **kwargs)

        return wrapped_function

    def notify(self):
        # logit只打日志，不做别的
        pass

# 这个实现有一个附加优势，在于比嵌套函数的方式更加整洁，而且包裹一个函数还是使用跟以前一样的语法
@logit()
def myfunc1():
    pass


# 继承，创建子类
class email_logit(logit):
    '''
    一个logit的实现版本，可以在函数调用时发送email给管理员
    '''

    def __init__(self, email='admin@myproject.com', *args, **kwargs):
        self.email = email
        super(email_logit, self).__init__(*args, **kwargs)

    def notify(self):
        # 发送一封email到self.email
        # 这里就不做实现了
        pass

# 从现在起，@email_logit 将会和 @logit 产生同样的效果，但是在打日志的基础上，还会多发送一封邮件给管理员。

# 原文地址：https://eastlakeside.gitbooks.io/interpy-zh/content/decorators/



#补充
"""
use_logging 就是一个装饰器，它一个普通的函数，它把执行真正业务逻辑的函数 func 包裹在其中，
看起来像 foo 被 use_logging 装饰了一样，use_logging 返回的也是一个函数，
这个函数的名字叫 wrapper。在这个例子中，函数进入和退出时 ，被称为一个横切面，这种编程方式被称为面向切面的编程。

@ 语法糖
如果你接触 Python 有一段时间了的话，想必你对 @ 符号一定不陌生了，没错 @ 符号就是装饰器的语法糖，
它放在函数开始定义的地方，这样就可以省略最后一步再次赋值的操作。


*args、**kwargs



带参数的装饰器
装饰器还有更大的灵活性，例如带参数的装饰器，在上面的装饰器调用中，该装饰器接收唯一的参数就是执行业务的函数 foo 。
装饰器的语法允许我们在调用时，提供其它参数，比如@decorator(a)。
这样，就为装饰器的编写和使用提供了更大的灵活性。比如，我们可以在装饰器中指定日志的等级，因为不同业务函数可能需要的日志级别是不一样的。


def use_logging(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == "warn":
                logging.warn("%s is running" % func.__name__)
            elif level == "info":
                logging.info("%s is running" % func.__name__)
            return func(*args)
        return wrapper

    return decorator

@use_logging(level="warn")
def foo(name='foo'):
    print("i am %s" % name)

foo()

上面的 use_logging 是允许带参数的装饰器。
它实际上是对原有装饰器的一个函数封装，并返回一个装饰器。我们可以将它理解为一个含有参数的闭包。
当我 们使用@use_logging(level="warn")调用的时候，Python 能够发现这一层的封装，并把参数传递到装饰器的环境中。

@use_logging(level="warn") 等价于 @decorator

类装饰器
没错，装饰器不仅可以是函数，还可以是类，相比函数装饰器，类装饰器具有灵活度大、高内聚、封装性等优点。
使用类装饰器主要依靠类的__call__方法，当使用 @ 形式将装饰器附加到函数上时，就会调用此方法。

class Foo(object):
    def __init__(self, func):
        self._func = func

    def __call__(self):
        print ('class decorator runing')
        self._func()
        print ('class decorator ending')

@Foo
def bar():
    print ('bar')

bar()
functools.wraps


使用装饰器极大地复用了代码，但是他有一个缺点就是原函数的元信息不见了，比如函数的docstring、__name__、参数列表，先看例子：


# 装饰器
def logged(func):
    def with_logging(*args, **kwargs):
        print func.__name__      # 输出 'with_logging'
        print func.__doc__       # 输出 None
        return func(*args, **kwargs)
    return with_logging

# 函数
@logged
def f(x):
   """does some math"""
   return x + x * x

logged(f)

from functools import wraps
def logged(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print func.__name__      # 输出 'f'
        print func.__doc__       # 输出 'does some math'
        return func(*args, **kwargs)
    return with_logging

@logged
def f(x):
   """does some math"""
   return x + x * x

装饰器顺序
一个函数还可以同时定义多个装饰器，比如：

@a
@b
@c
def f ():
    pass
    
f = a(b(c(f)))  
    
"""