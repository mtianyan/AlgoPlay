class SelectionSort:
    @staticmethod
    def sort(data_list):
        for i in range(len(data_list)):
            max_index = i
            for j in range(i, len(data_list)):
                if data_list[j] > data_list[max_index]:
                    max_index = j
            data_list[i], data_list[max_index] = data_list[max_index], data_list[i]

    @staticmethod
    def sort2(data_list):
        for i in range(len(data_list))[::-1]:
            min_index = i
            for j in range(0, len(data_list) - i):
                if data_list[j] < data_list[min_index]:
                    min_index = j
            data_list[i], data_list[min_index] = data_list[min_index], data_list[i]


if __name__ == '__main__':
    test_list = [1, 4, 2, 3, 6, 5]
    SelectionSort.sort(test_list)
    print(test_list)
    SelectionSort.sort2(test_list)
    print(test_list)
