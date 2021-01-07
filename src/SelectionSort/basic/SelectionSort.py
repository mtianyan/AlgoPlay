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
