from typing import List
from typing import TypeVar, Generic

T = TypeVar('T')


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

    def get_last(self) -> List[T]:
        return self.get(self._size - 1)

    def get_first(self) -> List[T]:
        return self.get(0)

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
        del self._data[self._size]
        if self._size == self._capacity // 4 and self._capacity // 2 > 1:
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


class ArrayStack:
    def __init__(self, capacity):
        self.array = Array(capacity)

    def get_size(self):
        return self.array.get_size()

    def is_empty(self):
        return self.is_empty()

    def get_capacity(self):
        return self.array.get_capacity()

    def push(self, e):
        self.array.add_last(e)

    def pop(self):
        return self.array.remove_last()

    def peek(self):
        return self.array.get_last()

    def __str__(self):
        return f'size: {self.get_size()} capacity: {self.get_capacity()} ' + str(self.array) + "<-top"


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = ArrayStack(10)

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.data.push(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        tmp_list = ArrayStack(10)
        res = None
        for i in range(self.data.get_size()):
            if self.data.get_size() == 1:
                res = self.data.pop()
            else:
                tmp_list.push(self.data.pop())
        self.data = ArrayStack(10)
        for i in range(tmp_list.get_size()):
            self.data.push(tmp_list.pop())
        return res

    def peek(self) -> int:
        """
        Get the front element.
        """
        tmp_list = ArrayStack(10)
        for i in range(self.data.get_size()):
            if self.data.get_size() == 1:
                res = self.data.pop()
                tmp_list.push(res)
            else:
                tmp_list.push(self.data.pop())
        self.data = ArrayStack(10)
        for i in range(tmp_list.get_size()):
            self.data.push(tmp_list.pop())
        return res

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.data.get_size() == 0

    def __str__(self):
        return str(self.data)


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
print(obj)

param_2 = obj.pop()
print(param_2)
print(obj)

obj.push(2)

param_3 = obj.peek()
print(param_3)