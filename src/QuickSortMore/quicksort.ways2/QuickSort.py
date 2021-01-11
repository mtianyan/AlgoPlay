from random import randrange


class QuickSort:
    def sort(self, arr):
        return self._sort(arr, 0, len(arr) - 1)

    def _sort(self, arr, l, r):
        if l >= r:
            return
        p = self.partition(arr, l, r)
        self._sort(arr, l, p - 1)
        self._sort(arr, p + 1, r)

    def partition(self, arr, l, r):
        # 生成[l,r]随机索引
        p = randrange(l, r)
        arr[l], arr[p] = arr[p], arr[l]
        # arr[l+1...j] < v ; arr[j+1...i] >= v
        j = l
        for i in range(l + 1, r + 1):
            if arr[i] < arr[l]:
                j += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[l], arr[j] = arr[j], arr[l]
        return j

    def sort_two_ways(self, arr):
        return self._sort_two_ways(arr, 0, len(arr) - 1)

    def _sort_two_ways(self, arr, l, r):
        if l >= r:
            return
        p = self.partition2(arr, l, r)
        self._sort_two_ways(arr, l, p - 1)
        self._sort_two_ways(arr, p + 1, r)

    def partition2(self, arr, l, r):
        # 生成[l,r]随机索引
        p = randrange(l, r)
        arr[l], arr[p] = arr[p], arr[l]

        # arr[l+1...i-1] < v ; arr[j+1...r] >= v
        i = l + 1
        j = r
        while 1:
            # 虽然两重循环，其实只遍历了一遍O(n)
            while i <= j and arr[i] < arr[l]:
                # 从左往右
                i += 1
            while j >= i and arr[j] > arr[l]:
                # 从右往左
                j -= 1
            if i >= j:
                break
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        # 标定点放到数组的中间
        arr[l], arr[j] = arr[j], arr[l]
        return j


if __name__ == '__main__':
    import ArrayGenerator
    import SortingHelper
    import copy

    data = ArrayGenerator.ArrayGenerator.generate_random_array(10, 10)
    data = [7, 1, 4, 2, 8, 3, 6, 5]
    data_copy = copy.deepcopy(data)
    print(data)
    # SortingHelper.sort_test("MergeSort", data)
    # data = copy.deepcopy(data)
    SortingHelper.sort_test("QuickSort", data)
    print(data)

    SortingHelper.sort_test("QuickSort2Ways", data_copy)
    print(data)
    data_size = [10000, 100000]

    for size in data_size:
        input_data = ArrayGenerator.ArrayGenerator.generate_random_array(size, size)
        SortingHelper.sort_test("QuickSort", input_data)
        input_data = ArrayGenerator.ArrayGenerator.generate_ordered_array(size)
        SortingHelper.sort_test("QuickSort", input_data)
        input_data = ArrayGenerator.ArrayGenerator.generate_random_array(size, 1)
        SortingHelper.sort_test("QuickSort2Ways", input_data)
