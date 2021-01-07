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

    def add_last(self, e):
        self.add(self._size, e)
        # if self.is_empty():
        #     self._data = [e]
        # else:
        #     self._data.append(e)
        # self._size = self._size + 1

    def add(self, index, e):
        if self._size == self._capacity:
            raise ValueError("array is full")
        if index < 0 or index > self._size:
            raise ValueError("index error")
        for i in range(len(self._data)-1)[::-1]:
            if i >= index:
                self._data[i + 1] = self._data[i]
        self._data[index] = e
        self._size = self._size + 1

    def is_empty(self):
        return self._size == 0

    def __str__(self):
        return str(self._data)


if __name__ == '__main__':
    a = Array(3)
    a.add_last(1)
    a.add_last(2)
    a.add(1, 3)
    print(a)
