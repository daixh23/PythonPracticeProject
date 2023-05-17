# 函数 具备输入，处理，输出的功能。
# print函数
print('Hello,', 'jack', 'mike', '...', 'and all you guys!')

name = 'Ann'
age = '22'
print(f'{name} is {age} years old.')

# 官方文档 https://docs.python.org/3/library/functions.html#print
# print(*object, sep=' ', end='\n', file=sys.stdout, flush=False)


#####################################
# 关键字参数
# 在python中，函数的参数有两种：
#  - 位置参数 (Positional Argument): 在官方文档里常被缩写为arg
#  - 关键字参数 (Keyword Argument): 在官方文档里常被缩写为kwarg
#  - 可选位置参数 (Optional Positional Argument) - 比如 pow(x,y[,z])
#  - 可接收很多值得位置参数 *object
#####################################