from typing import List
from typing import TypeVar, Generic

T = TypeVar('T')


class Student:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

    def __repr__(self):
        return self.name


class Array(Generic[T]):
    _data: List[T] = []
    _size = 0

    def __init__(self, capacity=10):
        self._data = [None for one in range(capacity)]
        self._capacity = capacity

    def get_size(self):
        return self._size

    def get_capacity(self):
        return self._capacity

    def add_first(self, e: T):
        self.add(0, e)

    def add_last(self, e: T):
        self.add(self._size, e)
        # if self.is_empty():
        #     self._data = [e]
        # else:
        #     self._data.append(e)
        # self._size = self._size + 1

    def get(self, index) -> List[T]:
        if index < 0 or index >= self._size:
            raise ValueError("get index error")
        return self._data[index]

    def set(self, index, e: T) -> None:
        if index < 0 or index >= self._size:
            raise ValueError("get index error")
        self._data[index] = e

    def contains(self, e: T) -> bool:
        for index, one in enumerate(self._data[:self._size]):
            if one == e:
                return True
        return False

    def find(self, e: T) -> int:
        for index, one in enumerate(self._data[:self._size]):
            if one == e:
                return index
        return -1

    def remove(self, index) -> T:
        if index < 0 or index > self._size:
            raise ValueError("index error")
        ret = self._data[index]
        for i in range(len(self._data) - 1):
            if index <= i < self._size - 1:
                # print(f'{self._data[i]} = {self._data[i + 1]}')
                self._data[i] = self._data[i + 1]
        # print(self._data)
        self._size = self._size - 1
        self._data[self._size] = None
        if self._size == self._capacity // 2:
            self._resize(self._capacity // 2)
        return ret

    def remove_first(self) -> T:
        return self.remove(0)

    def remove_last(self) -> T:
        return self.remove(self._size - 1)

    def add(self, index, e: T):
        if self._size == self._capacity:
            self._resize(self._capacity * 2)
            # raise ValueError("array is full")
        if index < 0 or index > self._size:
            raise ValueError("index error")
        for i in range(len(self._data) - 1)[::-1]:
            if i >= index:
                self._data[i + 1] = self._data[i]
        self._data[index] = e
        self._size = self._size + 1

    def remove_element(self, e: T) -> None:
        index = self.find(e)
        if index != -1:
            self.remove(index)

    def is_empty(self):
        return self._size == 0

    def __str__(self):
        return f'Array size: {self._size} capacity: {self._capacity} {str([one for one in self._data if one])}'

    def _resize(self, new_capacity):
        new_data = [None for one in range(new_capacity)]
        for i, one in enumerate(self._data[:new_capacity]):
            new_data[i] = one
        self._data = new_data
        self._capacity = new_capacity


if __name__ == '__main__':
    a: Array[int] = Array(5)
    a.add_last(1)
    a.add_last(2)
    a.add(1, 3)
    print(a)
    a.add_first(4)
    a.add_last(-1)
    a.set(4, 88)
    print(a.contains(88))
    print(a.find(88))
    print(a)
    a.add_last(99)
    print("add_last", a)
    a.remove(4)
    print("remove-4", a)
    a.remove_last()
    print("remove_last", a)
    a.remove_first()
    print("remove_first", a)
    a.remove_element(3)
    print("remove_element", a)

    student_list: Array[Student] = Array(5)
    student_list.add_last(Student('mtianyan1'))
    student_list.add_last(Student('mtianyan2'))
    student_list.add(1, Student('mtianyan3'))
    print(student_list)
    student_list.add_first(Student('mtianyan4'))
    student_list.add_last(Student('mtianyan5'))
    student_list.set(4, Student('mtianyan88'))
    print(student_list.contains(Student('mtianyan88')))
    print(student_list.find(Student('mtianyan88')))
    print(student_list)
    student_list.remove(4)
    print("remove-4", student_list)
    student_list.remove_last()
    print("remove_last", student_list)
    student_list.remove_first()
    print("remove_first", student_list)
    student_list.remove_element(Student('mtianyan3'))
    print("remove_element", student_list)
