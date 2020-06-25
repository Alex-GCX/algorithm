def insert_sort(items):
    """插入排序"""
    # 最优时间复杂度: O(n), 原列表就是有序列表时, 遍历一遍, 无序部分的值都比有序部分的最大值要大, 即不会进入第二层循环
    # 最坏时间复杂度: O(n^2), 原列表是倒序的, 无序部分的值都比有序部分的最小值还小 n+(n-1+1)+(n-2+2)...+(n-n+n) = n*n = O(n^2)
    # 稳定性: 稳定(相同值不会交换)
    # 算法: 将列表分为左边有序, 右边无序的两部分, 从左往右遍历无序的数组, 将每次遍历到的元素, 插入前面的有序部分中
    #       插入的方式为从大到小依次比较有序部分, 若比有序最大值小, 则替换改值和最大值, 继续比较该值和第二大值, 直到遇到比该值小的元素停止比较

    # 从左往右遍历无序的数组
    for i in range(1, len(items)):
        # 获取到无序部分的元素, 遍历有序部分, 将获取的元素插入前面有序部分中
        while i > 0 and items[i] < items[i - 1]:
            items[i], items[i - 1] = items[i - 1], items[i]
            i -= 1


if __name__ == '__main__':
    items = [4, 39, 29, 20, 3, 7, 90, 56, 20]
    print(items)
    # items = [4, 19, 39]
    insert_sort(items)
    print(items)