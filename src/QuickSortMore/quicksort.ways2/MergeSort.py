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
        temp = copy.deepcopy(arr[l: r+1])
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


if __name__ == '__main__':
    import ArrayGenerator, SortingHelper

    data_size = [10000, 100000]

    for size in data_size:
        input_data = ArrayGenerator.generate_random_array(size, size)
        sort_test("SelectionSort", input_data)
        input_data = copy.deepcopy(input_data)
        sort_test("InsertionSort", input_data)
        input_data = copy.deepcopy(input_data)
        sort_test("MergeSort", input_data)
