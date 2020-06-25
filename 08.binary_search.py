def binary_search(items, item):
    """二分法查找, 切片递归"""
    # 最优时间复杂度: O(1), 刚好要找的数就在中间
    # 最坏时间复杂度: O(logn), 一直对半拆分, 直到拆到最后一层才找到元素, 共拆分了logn次
    # 说明: 只能针对有序列表进行二分法查找
    # 算法: 将有序列表对半拆分, 比较中间的元素和要找的元素, 若相等, 则找到了, 若比中间元素大, 则将右边列表切片出来递归调用, 继续寻找
    #       使用切片只能判断元素是否在列表中, 而不能返回元素在列表中的下标位置

    # 获取长度
    length = len(items)
    # 若长度为0, 则说明不存在该列表中
    if length < 1:
        return False
    # 对半分找到中间元素
    mid = length // 2
    # 比较中间元素和所找元素
    if item == items[mid]:
        return True
    elif item > items[mid]:
        return binary_search(items[mid + 1:], item)
    else:
        return binary_search(items[:mid], item)


def binary_search_2(items, item, start=0, end=None):
    """二分法查找, 原列表递归"""
    # 最优时间复杂度: O(1), 刚好要找的数就在中间
    # 最坏时间复杂度: O(logn), 一直对半拆分, 直到拆到最后一层才找到元素, 共拆分了logn次
    # 说明: 只能针对有序列表进行二分法查找
    # 算法: 将有序列表对半拆分, 比较中间的元素和要找的元素, 若相等, 则找到了, 若比中间元素大, 则将右边列表部分进行递归调用, 继续寻找

    # 获取长度
    length = len(items)
    # 初始化end
    if end is None:
        end = length
    # 若起始位置和结束位置相同, 则说明没有找到
    if start == end:
        return False
    # 获取中间位置
    mid = (start+end) // 2
    # 比较中间元素和所找元素
    if item == items[mid]:
        return mid
    elif item > items[mid]:
        return binary_search_2(items, item, mid+1, end)
    else:
        return binary_search_2(items, item, start, mid)


if __name__ == '__main__':
    items = [3, 4, 7, 20, 20, 29, 39, 56, 90]
    item = 56
    print(binary_search(items, item))
    print(binary_search_2(items, item))
