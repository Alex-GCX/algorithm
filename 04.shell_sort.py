def shell_sort(items):
    """希尔排序"""
    # 最优时间复杂度: 视步长选择而定
    # 最坏时间复杂度: O(n^2)
    # 稳定性: 不稳定, 分为不同组之后交换操作不能保证前后次序不变
    # 算法: 在普通的插入排序基础上, 增加步长的概念, 理解为普通插入排序的步长即为1, 每次比较交换时, 和前一个元素比较
    #       而希尔排序中, 每次比较交换时, 和前一个步长的元素比较, 这样就相当于将列表分割成了几部分, 对每部分依次进行插入排序
    #       再比较完一遍后, 缩短步长, 再进行步长比较交换, 直到步长为1

    # 列表长度
    length = len(items)
    # 步长
    step = length // 2
    # step变化到0之前, 插入算法执行的次数
    while step > 0:
        # 插入算法, 与普通的插入算法区别就是step步长
        for i in range(step, length):
            while i > 0 and items[i] < items[i-step]:
                items[i], items[i-step] = items[i-step], items[i]
                i -= step
        # 缩短step步长
        step = step // 2


if __name__ == '__main__':
    items = [7, 39, 29, 20, 3, 4, 90, 56, 20]
    # items = [4, 3, 29, 20, 29, 39, 90, 56, 20]
    print(items)
    shell_sort(items)
    print(items)
