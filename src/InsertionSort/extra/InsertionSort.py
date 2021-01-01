from ArrayGenerator import ArrayGenerator
from SortingHelper import sort_test, is_sort


class InsertionSort:
    @staticmethod
    def sort(arr):
        for i in range(len(arr))[::-1]:
            t = arr[i]
            print(t)
            # j = i-1
            for j in range(i, len(arr)):
                if t > arr[j]:
                    print("t", t, "arr[j]", arr[j])
                    arr[j - 1] = arr[j]
                else:
                    break
            print("jj", j)
            arr[j] = t
            print("arr_end", arr)


if __name__ == '__main__':
    test_list = [2, 4, 6, 3, 1, 5]
    InsertionSort.sort(test_list)
    print(test_list)

    data_size = [10000]

    for size in data_size:
        input_data = ArrayGenerator.generate_random_array(size, size)
        sort_test("random InsertionSort", input_data)
        input_data = ArrayGenerator.generate_ordered_array(size)
        sort_test("order InsertionSort", input_data)
