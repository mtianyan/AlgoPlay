class Sum:
    def sum(self, arr):
        return Sum._sum(arr, 0)

    # 计算arr[l..n)这个区间内所有数字的和
    @staticmethod
    def _sum(arr, location):
        if location == len(arr):
            return 0
        return arr[location] + Sum._sum(arr, location + 1)


if __name__ == '__main__':
    print(Sum().sum([1, 2, 3, 4, 5, 6, 7, 8]))
