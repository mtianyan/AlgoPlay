from ArrayGenerator import ArrayGenerator
from SortingHelper import sort_test


class InsertionSort:
    @staticmethod
    def sort(data_list):
        for i in range(len(data_list)):
            for j in range(1, i + 1)[::-1]:
                if data_list[j] < data_list[j - 1]:
                    data_list[j - 1], data_list[j] = data_list[j], data_list[j - 1]


if __name__ == '__main__':
    test_list = [6, 4, 2, 3, 1, 5]
    InsertionSort.sort(test_list)
    print(test_list)
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
    
    
    """
