def is_sort(data_list):
    for i in range(1, len(data_list)):
        # print(i)
        if data_list[i - 1] > data_list[i]:
            return False
    return True


def sort_test(sort_name, arr):
    import time
    start = time.time()
    if sort_name == "SelectionSort":
        import SelectionSort
        # for index in range(100):
        SelectionSort.SelectionSort.sort(arr)
    elif sort_name == "InsertionSort":
        import InsertionSort
        InsertionSort.InsertionSort.sort(arr)
    elif sort_name == "MergeSort":
        import MergeSort
        print(MergeSort.MergeSort.sort(arr))
    elif sort_name == "QuickSort":
        import QuickSort
        print(QuickSort.QuickSort().sort(arr))
    elif sort_name == "QuickSort2Ways":
        import QuickSort
        print(QuickSort.QuickSort().sort_two_ways(arr))
    if not is_sort(arr):
        raise RuntimeError(f"{sort_name} 未排序成功")
    end = time.time()
    print(f'{sort_name}, size: {len(arr)} : {end - start} s')


if __name__ == '__main__':
    print(is_sort([1, 2, 3]))
    print(is_sort([1, 3, 3, 4, 5, 2]))
