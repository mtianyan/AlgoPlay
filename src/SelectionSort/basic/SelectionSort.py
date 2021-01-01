class SelectionSort:
    @staticmethod
    def sort(data_list):
        for i in range(len(data_list)):
            min_idx = i
            print("min_idx", min_idx)
            for j in range(i + 1, len(data_list)):
                if data_list[j] < data_list[min_idx]:
                    min_idx = j
                    print("min_idx_change", min_idx)
            print(data_list[i], data_list[min_idx], "被交换")
            data_list[i], data_list[min_idx] = data_list[min_idx], data_list[i]
        return data_list


if __name__ == '__main__':
    test_list = [1, 4, 2, 3, 6, 5]
    print(SelectionSort.sort(test_list))
