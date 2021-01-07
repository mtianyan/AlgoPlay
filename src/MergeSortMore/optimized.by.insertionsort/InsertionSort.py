from ArrayGenerator import ArrayGenerator
from SortingHelper import sort_test
import copy


class InsertionSort:
    @staticmethod
    def sort(arr):
        for i in range(len(arr)):
            # print("i", i)
            t = arr[i]
            j = i
            for j in range(1, i + 1)[::-1]:
                # print("j", j)
                if t < arr[j - 1]:
                    arr[j] = arr[j - 1]
                else:
                    break
                if j == 1:
                    j = j-1
            # print("change_j", j)
            # if arr == [2, 2, 3, 4, 6, 5]:
            #     print("debug")
            # print(arr)
            arr[j] = t
            # print("end_arr", arr)

    @staticmethod
    def sort2(arr,l,r): # TODO 改造插入排序
        for i in range(len(arr)):
            # print("i", i)
            t = arr[i]
            j = i
            for j in range(1, i + 1)[::-1]:
                # print("j", j)
                if t < arr[j - 1]:
                    arr[j] = arr[j - 1]
                else:
                    break
                if j == 1:
                    j = j-1
            # print("change_j", j)
            # if arr == [2, 2, 3, 4, 6, 5]:
            #     print("debug")
            # print(arr)
            arr[j] = t
            # print("end_arr", arr)

if __name__ == '__main__':
    test_list = [6, 4, 2, 3, 1, 5]
    InsertionSort.sort(test_list)
    print(test_list)
    data_size = [10000, 100000]

    for n in data_size:
        # print("Random Array : ")
        # arr = ArrayGenerator.generate_random_array(n, n)
        # arr2 = copy.deepcopy(arr)
        # print(arr2[:10])
        # sort_test("InsertionSort", arr)
        # sort_test("SelectionSort", arr2)

        print("Ordered Array : ")
        arr = ArrayGenerator.generate_ordered_array(n)
        arr2 = copy.deepcopy(arr)
        print(arr2[:10])
        sort_test("InsertionSort", arr)
        sort_test("SelectionSort", arr2)

        """
        InsertionSort, size: 10000 : 0.009609222412109375 s
        SelectionSort, size: 10000 : 3.472014904022217 s
        """