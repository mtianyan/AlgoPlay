from typing import List
from abc import abstractmethod
from typing import TypeVar, Protocol


class Student:
    def __init__(self, score):
        self.score = score

    def __lt__(self, other):
        return self.score < other.score

    def __str__(self):
        return f"student-score: {self.score}"

    def __repr__(self):
        return f"student-score: {self.score}"


class Comparable(Protocol):
    """Protocol for annotating comparable types."""

    @abstractmethod
    def __lt__(self, other) -> bool:
        pass


CT = TypeVar("CT", bound=Comparable)


class SelectionSort:
    @staticmethod
    def sort(data_list: List[CT]):
        for i in range(len(data_list)):
            min_idx = i
            for j in range(i + 1, len(data_list)):
                if data_list[j] < data_list[min_idx]:
                    min_idx = j
            data_list[i], data_list[min_idx] = data_list[min_idx], data_list[i]


if __name__ == '__main__':
    test_list: List[int] = [1, 4, 2, 3, 6, 5]
    SelectionSort.sort(test_list)
    student_list: List[Student] = [Student(98), Student(98), Student(100), Student(96)]
    SelectionSort.sort(student_list)
    print(student_list)  # __repr__
    for one in student_list:  # __str__
        print(one)
