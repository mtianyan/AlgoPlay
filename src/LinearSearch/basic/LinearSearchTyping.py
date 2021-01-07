from typing import List


class LinearSearch:
    @staticmethod
    def search(data: List[int], target: int) -> int:
        for index, one in enumerate(data):
            if one == target:
                return index
        return -1


if __name__ == '__main__':
    test_list: List[int] = [24, 18, 12, 9, 16, 66, 32, 1]
    print(LinearSearch.search(test_list, 16))
    print(LinearSearch.search(test_list, 666))
