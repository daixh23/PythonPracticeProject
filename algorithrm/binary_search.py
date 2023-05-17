# 如果是顺次比较，对于一个长度为n的数组，最多需要比较n次，这被称为线性时间（linear time) / 算法复杂度 O(n)
# 二分查找则不同，运行时间是为对数时间（log时间），前提是数组是排序过的 / 算法复杂度 O(log n)
# 五种 大O 运行时间
#   O(log n) 对数时间 典型是二分查找
#   O(n) 线性时间 - 简单查找
#   O(n*log n) - 快速排序 速度较快的排序算法
#   O(n2) - 选择排序 速度较慢的排序算法
#   O（n!) - 旅行商问题 - 非常慢的算法 - n的阶乘
def binary_search(data, target):
    target_index = -1
    start_index = 0
    end_index = len(data) - 1

    while True:
        middle_index = (start_index + end_index) // 2
        middle_value = data[middle_index]
        length = end_index + 1 - start_index
        print(f"middle_index: {middle_index}, middel_value:{middle_value}, length: {length}")

        if target == middle_value:
            target_index = middle_index
            break
        # should in the right side
        elif target > middle_value:
            start_index = middle_index + 1
        # should in the left side
        else:
            end_index = middle_index - 1
        # ending loop, if all not match
        if not length:
            break
    return target_index

if __name__ == '__main__':
    a = [1, 2, 3, 5, 8, 9, 10, 12, 14, 15, 16]
    t_index = binary_search(a, 11)
    print(t_index)
