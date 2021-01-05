def _sum(arr, start):
    if start == len(arr):
        return 0
    return arr[start] + _sum(arr, start + 1)


def sum(arr):
    return _sum(arr, 0)


if __name__ == '__main__':
    print(sum([1, 2, 3]))
