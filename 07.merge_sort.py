def merge_sort(items):
    """归并排序"""
    # 最优时间复杂度: O(nlogn), 拆分时, 只是进行切片, 没有循环, 时间复杂度为O(1), 经过logn次合并, 每次遍历n个元素
    # 最坏时间复杂度: O(nlogn), 拆分时, 只是进行切片, 没有循环, 时间复杂度为O(1), 经过logn次合并, 每次遍历n个元素
    # 稳定性: 稳定
    # 算法: 将列表对半拆分, 然后将左右两个新列表继续对半拆分, 直到拆成单个元素为一个单独的列表
    #       然后将拆开的部分再两两排序合并, 排序合并时, 合并逻辑为, 将两个指针分别指向左右两个列表的起始位置
    #       比较指针指向的元素大小, 将较小者放入新的结果列表中, 再将该指针右移, 继续比较大小, 比较完毕后, 该结果列表即为最终排序后的列表

    # 获取列表长度
    length = len(items)
    if length <= 1:
        return items
    # 拆分
    mid = length // 2
    left_list = merge_sort(items[:mid])
    right_list = merge_sort(items[mid:])
    # 合并
    left = 0
    right = 0
    result = []
    while left < len(left_list) and right < len(right_list):
        if left_list[left] <= right_list[right]:
            result.append(left_list[left])
            left += 1
        else:
            result.append(right_list[right])
            right += 1
    # 将结果列表拼上左右两列表的最后剩下的元素
    result += left_list[left:]
    result += right_list[right:]
    return result


if __name__ == '__main__':
    items = [7, 39, 29, 20, 3, 4, 90, 56, 20]
    # items = [4, 3, 29, 20, 29, 39, 90, 56, 20]
    print(items)
    print(merge_sort(items))
