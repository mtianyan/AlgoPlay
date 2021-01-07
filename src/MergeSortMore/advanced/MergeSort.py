import copy


class MergeSort:
    @staticmethod
    def sort(arr):
        return MergeSort._sort(arr, 0, len(arr) - 1)
        # 合并两个有序的区间 arr[l, mid] 和 arr[mid + 1, r]

    @staticmethod
    def _sort(arr, l, r):
        if l >= r:
            return
        mid = (l + r) // 2
        MergeSort._sort(arr, l, mid)
        MergeSort._sort(arr, mid + 1, r)
        MergeSort.merge(arr, l, mid, r)
        return arr

    @staticmethod
    def merge(arr, l, mid, r):
        temp = copy.deepcopy(arr[l: r + 1])
        i = l
        j = mid + 1
        # 每轮循环为 arr[k] 赋值
        for k in range(l, r+1):
            if i > mid:
                arr[k] = temp[j - l]
                j = j + 1
            elif j > r:
                arr[k] = temp[i - l]
                i = i + 1
            elif temp[i - l] <= temp[j - l]:
                arr[k] = temp[i - l]
                i = i + 1
            else:
                arr[k] = temp[j - l]
                j = j + 1

    @staticmethod
    def sort2(arr):
        temp = copy.deepcopy(arr)
        return MergeSort._sort2(arr, 0, len(arr) - 1, temp)
        # 合并两个有序的区间 arr[l, mid] 和 arr[mid + 1, r]

    @staticmethod
    def _sort2(arr, l, r, temp):
        if l >= r:
            return
        mid = (l + r) // 2
        MergeSort._sort2(arr, l, mid, temp)
        MergeSort._sort2(arr, mid + 1, r, temp)

        if arr[mid] > arr[mid+1]:
            MergeSort.merge2(arr, l, mid,r, temp)
        return arr

    @staticmethod
    def merge2(arr, l, mid, r, temp):
        temp[l:l+r-1+1] = arr[l:l+r-1+1]  #  System.arraycopy(arr, l, temp, l, r - l + 1);
        i = l
        j = mid + 1
        # 每轮循环为 arr[k] 赋值
        for k in range(l, r+1):
            if i > mid:
                arr[k] = temp[j]
                j = j + 1
            elif j > r:
                arr[k] = temp[i]
                i = i + 1
            elif temp[i - l] <= temp[j - l]:
                arr[k] = temp[i]
                i = i + 1
            else:
                arr[k] = temp[j]
                j = j + 1

if __name__ == '__main__':
    import ArrayGenerator, SortingHelper

    data = ArrayGenerator.ArrayGenerator.generate_random_array(10, 10)
    print(data)
    SortingHelper.sort_test("MergeSort", data)
    data = copy.deepcopy(data)
    SortingHelper.sort_test("MergeSort2", data)

    from SortingHelper import sort_test
    data_size = [10000, 100000]
#
    for size in data_size:
        input_data = ArrayGenerator.ArrayGenerator.generate_random_array(size, size)
        input_data = copy.deepcopy(input_data)
        sort_test("MergeSort", input_data)
        input_data = copy.deepcopy(input_data)
        sort_test("MergeSort2", input_data)
#     """
#     MergeSort, size: 10 : 0.009989738464355469 s
# SelectionSort, size: 10000 : 5.314520597457886 s
# InsertionSort, size: 10000 : 0.009989738464355469 s
# MergeSort, size: 10000 : 82.484299659729 s
#     """

"""
MergeSort, size: 10 : 0.001264810562133789 s
MergeSort2, size: 10 : 1.6927719116210938e-05 s
MergeSort, size: 10000 : 0.12834906578063965 s
MergeSort2, size: 10000 : 0.011030912399291992 s
MergeSort, size: 100000 : 1.571838140487671 s
MergeSort2, size: 100000 : 0.12029886245727539 s
"""