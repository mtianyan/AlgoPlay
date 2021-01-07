import copy


def gen_depth(depth):
    return (depth + 1) * "--"


class MergeSort:
    @staticmethod
    def sort(arr):
        return MergeSort._sort(arr, 0, len(arr) - 1, 0)
        # 合并两个有序的区间 arr[l, mid] 和 arr[mid + 1, r]

    @staticmethod
    def _sort(arr, l, r, depth):
        # // 生成深度字符串
        depth_str = gen_depth(depth)

        # 打印当前 sort 处理的数组区间信息
        print(depth_str, end=":")
        print(f"mergesort arr[{l}:{r}]")
        if l >= r:
            return
        mid = (l + r) // 2
        MergeSort._sort(arr, l, mid, depth + 1)
        MergeSort._sort(arr, mid + 1, r, depth + 1)

        # 打印这次 merge 要处理的区间范围
        print(depth_str, end=":")
        print(f"merge sort arr[{l}:{mid}] and arr[{mid + 1}:{r}]")
        MergeSort.merge(arr, l, mid, r)

        # 打印 merge 后的数组
        print(depth_str, end=":")
        print(f"after mergesort arr[{l}:{r}]")
        print(arr)
        return arr

    @staticmethod
    def merge(arr, l, mid, r):
        temp = copy.deepcopy(arr[l: r+1])
        i = l
        j = mid + 1
        # 每轮循环为 arr[k] 赋值
        for k in range(l, r + 1):
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

    data = ArrayGenerator.ArrayGenerator.generate_random_array(10, 10)
    data = [7, 1, 4, 2, 8, 3, 6, 5]
    print(data)
    SortingHelper.sort_test("MergeSort", data)
    # from SortingHelper import sort_test
    data_size = [10000, 100000]
    data_size = [10000]

    for size in data_size:
        input_data = ArrayGenerator.ArrayGenerator.generate_random_array(size, size)
        SortingHelper.sort_test("SelectionSort", input_data)
        input_data = copy.deepcopy(input_data)
        SortingHelper.sort_test("InsertionSort", input_data)
        # input_data = copy.deepcopy(input_data)
        # SortingHelper.sort_test("MergeSort", input_data)
        """
        SelectionSort, size: 10000 : 3.4736220836639404 s
        InsertionSort, size: 10000 : 0.009485960006713867 s
        MergeSort, size: 10000 : 10.865494012832642 s
        """