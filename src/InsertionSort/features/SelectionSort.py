from ArrayGenerator import ArrayGenerator
from SortingHelper import sort_test


class SelectionSort:
    @staticmethod
    def sort(data_list):
        for i in range(len(data_list)):
            min_idx = i
            for j in range(i + 1, len(data_list)):
                if data_list[j] < data_list[min_idx]:
                    min_idx = j
            data_list[i], data_list[min_idx] = data_list[min_idx], data_list[i]
        return data_list

    @staticmethod
    def sort2(data_list):
        for i_index, one in enumerate(data_list):
            min_idx = i_index
            for j_index, j_one in enumerate(data_list[i_index:], i_index):
                if j_one < data_list[min_idx]:
                    min_idx = j_index
            data_list[i_index], data_list[min_idx] = data_list[min_idx], data_list[i_index]
        return data_list


if __name__ == '__main__':
    test_list = [1, 4, 2, 3, 6, 5]
    print(SelectionSort.sort(test_list))
    test_list = [1, 4, 2, 3, 6, 5]
    print(SelectionSort.sort2(test_list))
    data_size = [10000, 100000]

    for size in data_size:
        input_data = ArrayGenerator.generate_random_array(size, size)
        sort_test("SelectionSort", input_data)
    """
    java
    SelectionSort , n = 10000 : 0.123313 s
    SelectionSort , n = 100000 : 10.184974 s
    
    python
    SelectionSort, size: 10000 : 3.543562889099121 s
    SelectionSort, size: 10000 : 383.543562889099121 s
    """