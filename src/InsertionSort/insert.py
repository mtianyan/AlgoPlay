def insertion_sort(seq):
    """ 每次挑选下一个元素插入已经排序的数组中,初始时已排序数组只有一个元素"""
    n = len(seq)
    print(seq)
    for i in range(1, n):
        value = seq[i]  # 保存当前位置的值，因为转移的过程中它的位置可能被覆盖
        # 找到这个值的合适位置，使得前边的数组有序 [0,i] 有序
        pos = i
        while pos > 0 and value < seq[pos - 1]:
            seq[pos] = seq[pos - 1]  # 如果前边的元素比它大，就让它一直前移
            pos -= 1
        seq[pos] = value  # 找到了合适的位置赋值就好
        print(seq)


def insertion_sort2(seq):
    """ 每次挑选下一个元素插入已经排序的数组中,初始时已排序数组只有一个元素"""
    n = len(seq)
    print(seq)
    for i in range(n)[::-1]:
        value = seq[i]  # 保存当前位置的值，因为转移的过程中它的位置可能被覆盖
        # 找到这个值的合适位置，使得前边的数组有序 [i,n] 有序
        pos = i
        while pos < n-1 and value > seq[pos + 1]:
            seq[pos] = seq[pos + 1]  # 如果前边的元素比它大，就让它一直前移
            pos += 1
        seq[pos] = value  # 找到了合适的位置赋值就好
        print(seq)


if __name__ == '__main__':
    seq = [1, 7, 3, 0, 9, 4, 8, 2, 6, 5]
    # insertion_sort(seq)
    insertion_sort2(seq)
""" 不断把新元素放到已经有序的数组中
[1, 7, 3, 0, 9, 4, 8, 2, 6, 5]
[1, 7, 3, 0, 9, 4, 8, 2, 6, 5]
[1, 3, 7, 0, 9, 4, 8, 2, 6, 5]
[0, 1, 3, 7, 9, 4, 8, 2, 6, 5]
[0, 1, 3, 7, 9, 4, 8, 2, 6, 5]
[0, 1, 3, 4, 7, 9, 8, 2, 6, 5]
[0, 1, 3, 4, 7, 8, 9, 2, 6, 5]
[0, 1, 2, 3, 4, 7, 8, 9, 6, 5]
[0, 1, 2, 3, 4, 6, 7, 8, 9, 5]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""
