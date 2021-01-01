from ArrayGenerator import ArrayGenerator
from SortingHelper import sort_test, is_sort


class InsertionSort:
    @staticmethod
    def sort(arr):
        for i in range(0, len(arr))[::-1]:  # for i in range(len(arr))[::-1]:
            print(i)
            large = arr[i]  # t = arr[i]
            j = i
            for j in range(i, len(arr) - 1):  # for j in range(i, len(arr)):
                print("j", j)
                print("large", large)
                if large > arr[j + 1]:
                    arr[j] = arr[j + 1]
                    if j + 1 == len(arr) - 1:
                        j = j + 1
                else:
                    break
            print("change ", j)
            arr[j] = large
            print(arr)
        return arr

    @staticmethod
    def sort2(arr):
        for i in range(len(arr))[::-1]:
            cur = arr[i]
            for j in range(i, len(arr)):
                if j < len(arr) - 1:
                    if cur > arr[j + 1]:
                        arr[j] = arr[j + 1]
                    else:
                        break
            arr[j] = cur


if __name__ == '__main__':
    test_list = [2, 4, 6, 3, 1, 5]
    InsertionSort.sort(test_list)
    print(test_list)
    # InsertionSort.sort2(test_list)
    # print(test_list)

    data_size = [10]

    for size in data_size:
        input_data = ArrayGenerator.generate_random_array(size, size)
        print(input_data)
        sort_test("InsertionSort", input_data)
    #     input_data = ArrayGenerator.generate_ordered_array(size)
    #     sort_test("order InsertionSort", input_data)
