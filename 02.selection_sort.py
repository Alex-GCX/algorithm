def selection_sort(items, start=0):
    """选择排序"""
    # 最优时间复杂度: O(n^2), n+(n-1)+(n-2)...+1 = (1+n)n/2 = O(n^2) 无论什么情况, 就需要递归找出右边部分的最小值
    # 最坏时间复杂度: O(n^2), n+(n-1)+(n-2)...+1 = (1+n)n/2 = O(n^2)
    # 稳定性: 看清况, 如果将最小元素放到左边, 即左边为有序的, 在前面的值依然在前面, 则是稳定的
    #                但是如果是将最大元素放到右边, 即右边为有序的, 那么在前面的元素就会先放到后面, 则是不稳定的
    #                解决方法为获取最大值时, 加上等号, 即将后面的值认为是最大值, 那么后面的值就会先排在后面
    # 算法: 将列表分为左边有序, 右边无序两部分, 遍历无序的部分, 选择最小的元素放到左边有序部分结尾

    # 获取列表长度
    length = len(items)
    # 遍历后最小元素的下标, 初始化为start
    min_index = start
    # 遍历无序部分, 获取最小值的下标
    for i in range(min_index+1, length):
        # 循环一遍, 获取到最小元素下标
        if items[i] < items[min_index]:
            min_index = i
    # 将起始值与最小值替换
    items[start], items[min_index] = items[min_index], items[start]
    # 将start右移, 递归调用, 遍历列表start右边部分
    start += 1
    if start != length - 1:
        selection_sort(items, start)


if __name__ == '__main__':
    items = [4, 39, 29, 20, 3, 7, 90, 56, 20]
    print(items)
    # items = [4, 19, 39]
    selection_sort(items)
    print(items)
