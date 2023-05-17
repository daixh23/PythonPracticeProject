#########################
# 流程控制由 分支 和 循环 组成。无论多么复杂的流程控制，都可以用这两个来实现，就好像无论多么复杂的电路，最终都是由开路和通路两个状态构成的一样。
# 1966年的论文 Flow diagrams, turing machines and languages with only two formation rules (Bohm, Jacopini)
# Wikipedia: Minimal structured control flow
#########################

#########################
# if 语句
#########################
import random
r = random.randrange(0, 13) # 生成的随机数从0开始
print(r)

if r == 7:
    print('Draw!')
elif r >= 2 and r < 7:
    print('Small!')
elif r > 7:
    print('Big!')
else:
    print('Not valid!')

#########################
# for 循环
# python语言中的 for 循环不使用像其他语言中那样的计数器，取而代之的是range() - 整数等差数列生成器
# range 是个内建函数，使用方式如下：
#  - range(stop) - 生成一个从0 到 stop-1的整数数列
#  - range(start, stop, [,step]) - step是步长 即等差数列中的差
#########################
for a in range(10):
    print(f'value of a: {a}')

print(list(range(10)))

print(list(range(1, 10, 2)))

# 还可以生成负数的数列
print(list(range(0, -10, -1)))

# 在循环中可以通过 continue 和 break来控制流程走向
# 如果出现continue语句，其后的语句将被忽略，并开始下一次循环
# 如果出现break语句，将从此结束当前循环，开始执行循环之后的语句
for n in range(2, 100):
    if n == 2:
        print(n)
        continue
    for i in range(2, n):
        if (n % i) == 0:
            break
    else:
        print(n) # for 语句块后还可以附加一个else语句块，这是python的一个比较有个性的地方，附加在for语句块结尾的else语句块，在没有break发生的情况下将会运行。

# pass 语句什么都不干
# 在写程序的时候，我们可以用pass去占位，然后先写别的部分，再回头过来补充本来应该写在pass所在位置的那一段代码。尤其是写嵌套的判断语句或者循环语句的时候，先用pass占位，然后逐一突破。
for i in range(100):
    pass
    if i % 2 == 0:
        pass

#########################
# while 循环
# 大多数编程语言都会提供两种循环结构：
#  - Collection-Controlled Loop (以集合为基础的循环) - for ... in ...
#  - Condition-Controlled Loop (以条件为基础的循环) - while
# for循环更适合处理序列类型数据(Sequence Type)的迭代，例如处理字符串中的每一个字符，把range()函数返回的数列作为某种序列类型的索引。
# while循环更为灵活，因为它后面只需要接一个逻辑表达式。
#########################
# 输出 1000 以内的斐波那契数列
n = 1000
a, b = 0, 1
while a < n:
    print(a, end=' ')
    a, b = b, a+b
print()