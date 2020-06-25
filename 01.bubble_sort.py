def bubble_sort(items, end=None):
    """冒泡排序"""
    # 最优时间复杂度: O(n), 原列表就是有序列表时, 遍历一遍, 没有发现需要交换的元素
    # 最坏时间复杂度: O(n^2), 原列表是倒序的, 每次都发生交换, n+(n-1)+(n-2)...+1 = (1+n)n/2 = O(n^2)
    # 稳定性: 稳定(相同值不会交换)
    # 算法: 从左往右交换相邻的两个元素, 将较大者放到右边, 这样每次循环一遍就会将最大者转移到最右边, 称为冒泡

    # 设置这一次需要遍历的长度
    if end is None:
        end = len(items)-1
    # 设置一个哨兵pivot, 用来达到最优时间复杂度, 即若原序列就是有序的, 那么按理说最优时间复杂度就是O(n)
    # 但是若无该哨兵, 则依然会继续递归调用, 而这些递归调用是没有意义的
    pivot = 0
    # 比较第一个和第二个数, 如果第一个数比第二个大, 则两者交换位置, 即两者大的放右边
    # 从左往右依次比较, 比较到倒数第二个数时, 一次列表的遍历完成, 这是结果是把最大的数放在列表最右边
    for i in range(end):
        if items[i] > items[i + 1]:
            items[i + 1], items[i] = (items[i], items[i + 1])
            # 若有交换, 则哨兵+1
            pivot += 1
    # 通过哨兵判断, 若无交换记录, 则说明已经是排好序了, 不需要再进行递归, 否则需要递归
    if pivot != 0:
        # 递归调用自身, 继续进行列表的遍历
        end -= 1
        if end != 1:
            bubble_sort(items, end)


if __name__ == '__main__':
    items = [4, 39, 29, 20, 3, 7, 90, 56, 20]
    print(items)
    # items = [4, 19, 39]
    bubble_sort(items)
    print(items)