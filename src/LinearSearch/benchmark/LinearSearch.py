from ArrayGenerator import ArrayGenerator
import time
import numpy as np

class LinearSearch:
    @staticmethod
    def search(data, target):
        for index, one in enumerate(data):
            if one == target:
                return index
        return -1


if __name__ == '__main__':
    test_list = [24, 18, 12, 9, 16, 66, 32, 4]
    print(LinearSearch.search(test_list, 16))
    print(LinearSearch.search(test_list, 666))
    data_size = [1000000, 10000000]
    for size in data_size:
        input_data = ArrayGenerator.generate_ordered_array(size)
        start = time.time()
        for index in range(100):
            LinearSearch.search(input_data, size-1)
        end = time.time()
        print(f'size: {size} 100 runs: {end - start} s')
        start = time.time()
        for index in range(100):
            input_data.index(size-1)
        end = time.time()
        print(f'size: {size} 100 runs: {end - start} s')
        start = time.time()
        dis = np.asarray(input_data)
        for index in range(100):
            np.where(dis == size-1)
        end = time.time()
        print(f'size: {size} 100 runs: {end - start} s')
        """
        java
        n = 1000000, 100 runs : 0.151034679s
        n = 10000000, 100 runs : 1.577177105s
        
        python
        size: 1000000 100 runs: 5.00646710395813 s
        size: 1000000 100 runs: 1.2663331031799316 s
        size: 1000000 100 runs: 0.12476086616516113 s
        size: 10000000 100 runs: 50.83130168914795 s
        size: 10000000 100 runs: 12.865715026855469 s
        size: 10000000 100 runs: 1.57948899269104 s
        """