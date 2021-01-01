from ArrayGenerator import ArrayGenerator
from SortingHelper import sort_test, is_sort


class InsertionSort:
    @staticmethod
    def sort2(arr):
        for i in range(len(arr)):
            print("i", i)
            t = arr[i]
            j = i
            for j in range(0, i + 1)[::-1]:
                print("j", j)
                if j > 0:
                    if t < arr[j - 1]:
                        arr[j] = arr[j - 1]
                    else:
                        break
                # if j == 1:
                #     j = j-1
            print("change_j", j)
            # if arr == [2, 2, 3, 4, 6, 5]:
            #     print("debug")
            print(arr)
            arr[j] = t
            print("end_arr", arr)

    @staticmethod
    def sort(data_list):
        for i in range(len(data_list)):  # [0,n)
            # print(i)
            for j in range(1, i + 1)[::-1]:
                if data_list[j] < data_list[j - 1]:
                    data_list[j - 1], data_list[j] = data_list[j], data_list[j - 1]


if __name__ == '__main__':
    test_list = [2, 4, 6, 3, 1, 5]
    InsertionSort.sort2(test_list)
    raise ValueError
    print(test_list)
    InsertionSort.sort(test_list)
    print(test_list)
    input_data = ArrayGenerator.generate_random_array(10000, 10000)
    import copy
    import time

    input_data2 = copy.deepcopy(input_data)
    start = time.time()
    InsertionSort.sort(input_data)
    end = time.time()
    is_sort(input_data)
    print(f'sort: {end - start} s')

    start = time.time()
    InsertionSort.sort2(input_data2)
    end = time.time()
    is_sort(input_data2)
    print(f'sort2: {end - start} s')

    """
    [1, 2, 3, 4, 5, 6]
    [1, 2, 3, 4, 5, 6]
    sort: 9.23288869857788 s
    sort2: 4.863631963729858 s
    """

    data_size = [10000, 100000]

    for size in data_size:
        input_data = ArrayGenerator.generate_random_array(size, size)
        sort_test("InsertionSort", input_data)
    """
    java:
    SelectionSort , n = 10000 : 0.103108 s
    SelectionSort , n = 100000 : 10.020195 s
    InsertionSort , n = 10000 : 0.157813 s
    InsertionSort , n = 100000 : 15.633680 s
    
    python:
    SelectionSort, size: 10000 : 3.543562889099121 s
    SelectionSort, size: 10000 : 383.543562889099121 s
    InsertionSort, size: 10000 : 9.609786987304688 s
    
    """
