class Array:
    _data = []
    _size = 0

    def __init__(self, capacity=10):
        self._data = [None for one in range(capacity)]
        self._capacity = capacity

    def get_size(self):
        return self._size

    def get_capacity(self):
        return self._capacity

    def add_first(self, e):
        self.add(0, e)

    def add_last(self, e):
        self.add(self._size, e)
        # if self.is_empty():
        #     self._data = [e]
        # else:
        #     self._data.append(e)
        # self._size = self._size + 1

    def get(self, index):
        if index < 0 or index >= self._size:
            raise ValueError("get index error")
        return self._data[index]

    def set(self, index, e):
        if index < 0 or index >= self._size:
            raise ValueError("get index error")
        self._data[index] = e

    def contains(self, e):
        for index, one in enumerate(self._data[:self._size]):
            if one == e:
                return True
        return False

    def find(self, e):
        for index, one in enumerate(self._data[:self._size]):
            if one == e:
                return index
        return -1

    def remove(self, index):
        if index < 0 or index > self._size:
            raise ValueError("index error")
        ret = self._data[index]
        for i in range(len(self._data) - 1):
            if index <= i < self._size - 1:
                # print(f'{self._data[i]} = {self._data[i + 1]}')
                self._data[i] = self._data[i + 1]
        # print(self._data)
        self._size = self._size - 1
        return ret

    def remove_first(self):
        return self.remove(0)

    def remove_last(self):
        return self.remove(self._size - 1)

    def add(self, index, e):
        if self._size == self._capacity:
            raise ValueError("array is full")
        if index < 0 or index > self._size:
            raise ValueError("index error")
        for i in range(len(self._data) - 1)[::-1]:
            if i >= index:
                self._data[i + 1] = self._data[i]
        self._data[index] = e
        self._size = self._size + 1

    def remove_element(self, e):
        index = self.find(e)
        if index != -1:
            self.remove(index)

    def is_empty(self):
        return self._size == 0

    def __str__(self):
        return f'Array size: {self._size} capacity: {self._capacity} {str([one for one in self._data[:self._size] if one])}'


if __name__ == '__main__':
    a = Array(5)
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
    a.remove(4)
    print("remove-4", a)
    a.remove_last()
    print("remove_last", a)
    a.remove_first()
    print("remove_first", a)
    a.remove_element(3)
    print("remove_element", a)