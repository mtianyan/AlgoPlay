from typing import List
from typing import TypeVar

T = TypeVar('T')


class Student:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name


class LinearSearch:
    @staticmethod
    def search(data: List[T], target: T) -> int:
        for index, one in enumerate(data):
            if one == target:
                return index
        return -1


if __name__ == '__main__':
    test_list: List[int] = [24, 18, 12, 9, 16, 66, 32, 1]
    print(LinearSearch.search(test_list, 16))
    print(LinearSearch.search(test_list, 666))
    student_list: List[Student] = [Student('Alice'), Student('mtianyan1'), Student('mtianyan')]
    mtianyan = Student('mtianyan')
    print(LinearSearch.search(student_list, mtianyan))
