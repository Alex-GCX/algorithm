def quick_sort(items, start=0, end=None):
    """快速排序"""
    # 最优时间复杂度: O(nlogn), 原列表就是有序列表时, 将中间值当做key, 依次进行平均拆分
    #                直到拆到只剩一个元素, 即n/2/2/....=1, 拆分次数为log2n, 每次low和high加起来移动n次, 复杂度即为 nlogn
    # 最坏时间复杂度: O(n^2), n+(n-1)+(n-2)...+1 = (1+n)n/2 = O(n^2)
    # 稳定性: 不稳定
    # 算法: 将第一个元素(item[start])当做基准值(key), 确定该元素在排序后应该处于的位置
    #       确定位置的方法为所有小于该值的元素都在其左边, 所有大于该值的元素都在其右边
    #       确定位置之后, 将列表分为左边部分和右边部分, 分别将两部分通过递归调用继续确定两部分的第一个元素的位置
    #       直到所有元素位置确定完, 即排序完成

    # 初始化end的值
    if end is None:
        end = len(items) - 1
    # 若起始位置不小于结束位置, 则停止该部分的排序
    if start >= end:
        return
    # 初始化左边部分指针
    low = start
    # 初始化右边部分指针
    high = end
    # 将第一个元素设为基准值, 后面逻辑为确定该基准值应该处于的位置
    key = items[start]
    # 循环移动两个指针
    while low < high:
        # 先将high指针向左移动, 当high指的元素值小于key值时, 停止移动
        if items[high] >= key:
            high -= 1
        # 然后将low指针向右移动, 当low指的元素值大于key值时, 停止移动
        elif items[low] <= key:
            low += 1
        # 当两个指针都停止移动时, 交换两个指针的元素, 那么就可以继续移动指针了
        else:
            items[low], items[high] = items[high], items[low]
    # 当low=high即指针相遇时, 相遇的位置即为基准值key应处于的正确位置
    # 将key值弹出, 插入low的位置
    items.insert(low, items.pop(start))
    # 分成两部分, 进行递归
    quick_sort(items, start, low - 1)
    quick_sort(items, low + 1, end)


if __name__ == '__main__':
    items = [7, 39, 29, 20, 3, 4, 90, 56, 20]
    print(items)
    quick_sort(items)
    print(items)
