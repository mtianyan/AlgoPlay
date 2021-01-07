class LinearSearch:
    @staticmethod
    def search(data, target):
        for index, one in enumerate(data):
            if one == target:
                return index
        return -1


if __name__ == '__main__':
    test_list = [24, 18, 12, 9, 16, 66, 32, 4]
    print(LinearSearch.search(test_list, 16))
    print(LinearSearch.search(test_list, 666))
