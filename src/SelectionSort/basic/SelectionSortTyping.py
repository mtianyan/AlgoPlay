from typing import List
from abc import abstractmethod
from typing import TypeVar, Protocol


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
    print(test_list)

