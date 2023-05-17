################################
# 从结构上看，一切计算机程序，都由且只由两个最基本的成分构成：
#  - 运算 Evaluation
#  - 流程控制 Control Flow
#  而值可分为 常量 Literal 和 变量 Variable


################################
# 在Python中，每个函数都有返回值，即便在定义一个函数的时候没有设定返回值，也会加上默认的返回值 None
################################
def f():
    pass
print(f())
print(print(f()))

################################
# 值的类型 包含三种最基本的数据类型
#  - 布尔值 Boolean Value
#  - 数字 Numbers：整数 Int，浮点数 Float， 复数 Complex Numbers
#  - 字符串 Strings
#  运算的一个默认法则：在通常情况下，只有类型相同的值才能互相运算。
#  所以，在不得不对不同类型的值进行运算之前，需要做类型转换(Type Casting)
#  转换为数字 比如 int() float()，转换为字符串 str(), 还有个type()函数用来查看某个值属于什么类型
################################
print(type(3))
print(type(3.0))
print(type('3.14'))
print(type(True))
print(type(range(10))) # range
print(type([1,2,3])) # list
print(type((1,2,3))) # tuple
print(type({1,2,3})) # set
print(type({'a':1, 'b':2, 'c':3})) # dict

################################
# 数值操作符的优先级：
#  - 对两个值进行操作的+ - 最低
#  - 优先级稍高的是 * / // %
#  - 优先级更高得是对单个值操作的 +，-
#  - 优先级最高的是 **

# 布尔值操作符的优先级：最低是or, 稍高是and，最高是not

# 逻辑操作符 < > <= >= != == 优先级高于布尔值的操作符，低于数值计算的操作符。

# 字符串操作符
#  - 拼接 + 和空格
#  - 拷贝 *
#  - 逻辑运算 in not in 以及 < > <= >= != == 
################################
print('test' + "String")
print('test' "String")
print('test' + "String!"*3)
print('o' in 'Awesome' and 'o' not in 'python')
print('a' < 'b') # 比较的unicode码。当对字符串进行比较时，将分别从两个字符串的第一个字符开始逐个比较 直到比较出来
print(ord('a'))
print(ord('b'))

################################
# 列表操作符
#  - 拼接 + 和空格
#  - 拷贝 *
#  - 逻辑运算 in not in 以及 < > <= >= != == 
################################
a_list = [1, 2, 3, 4, 5]
b_list = [1, 2, 3, 5]
c_list = ['ann', 'bob', 'cindy', 'dude', 'eric']
print(a_list >  b_list) 
print(10 not in a_list)
print ('ann' in c_list)

################################
# python 内建函数
# https://docs.python.org/3/library/functions.html
################################