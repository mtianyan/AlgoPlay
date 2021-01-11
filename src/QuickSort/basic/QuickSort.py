class QuickSort:
    def sort(self, arr):
        self._sort(arr, 0, len(arr) - 1)

    def _sort(self, arr, l, r):
        if l >= r:
            return
        p = self.partition(arr, l ,r)
        self._sort(arr, l, p-1)
        self._sort(arr, p+1, r)

    def partition(self, arr, l, r):
        # arr[l+1...j] < v ; arr[j+1...i] >= v
        j = l
        for i in range(l + 1, r+1):
            if arr[i] < arr[l]:
                j += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[l], arr[j] = arr[j], arr[l]
        return j

if __name__ == '__main__':
    import ArrayGenerator
    import SortingHelper
    import copy
    data = ArrayGenerator.ArrayGenerator.generate_random_array(10, 10)
    data = [7, 1, 4, 2, 8, 3, 6, 5]
    print(data)
    # SortingHelper.sort_test("MergeSort", data)
    data = copy.deepcopy(data)
    SortingHelper.sort_test("QuickSort", data)
    print(data)