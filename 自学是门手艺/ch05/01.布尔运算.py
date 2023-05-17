###################################
# 逻辑操作符 也可称 比较操作符
###################################
# == 等于
print(1 == 2)

# != 不等于
print(1 != 2)

# > 大于
print(1 > 2)

# >= 大于等于
print(1 >= 1)

# < 小于
print(1 < 2)

# <= 小于等于
print(1 <= 2)

# in 属于
print('a' in 'basic')


###################################
# 布尔运算符 就三种
# 与 and
# 或 or
# 非 not
# 注意 True 和 False的头字母需要大写
###################################
print('(True and False) 结果是：', True and False);
print('(True and True) 结果是：', True and True);
print('(False and True) 结果是：', False and True);
print('(False and False) 结果是：', False and False);
print('(True or False) 结果是：', True or False);
print('(False or True) 结果是：', False or True);
print('(True or True) 结果是：', True or True);
print('(False or False) 结果是：', False or False);
print('(not True) 结果是：', not True);
print('(not False) 结果是：', not False);

###################################
# 流程控制
###################################
import random
r = random.randrange(1, 1000)
# 引入随机数，然后，每次执行程序的时候，r的值会不同

if r % 2 == 0:
    print(r, 'is even.')
else:
    print(r, 'is odd.')


###################################
# 循环
# 打印出100以内所有的质数 (Prime Number)
# 质数的定义， 它大于等于2，且只有在以它自身或者1为除数时余数为0.
###################################
for n in range(2, 100):
    if n == 2:
        print(n)
        continue
    for i in range(2, n):
        if (n % i) == 0:
            break
    # 注意这个缩进，这个else不是if的else 而是第二个for循环的else
    else:
        print(n)

###################################
# 算法优化
# 从以2为除数开始尝试，试到根号n之后的一个整数
###################################
for n in range(2, 100):
    if n == 2:
        print(n)
        continue
    for i in range(2, int(n ** 0.5)+1):
        if (n % i) == 0:
            break
    else:
        print(n)

###################################
# 函数
# 函数包括 函数名 Function Name，参数 Parameter，返回值 Return value，调用 Call
# 被调用的函数也可以理解为子函数
###################################
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for m in range(2, int(n ** 0.5)+1):
        if (n % m) == 0:
            return False
    else:
        return True

for i in range(80, 110):
    if is_prime(i):
        print(i)


###################################
# 操作符
# + - * / 加减乘除
# // 商
# % 余
# ** 幂
# 赋值符号与操作符的连用
###################################
x = 11
x %= 3 # x = x % 3
print(x)