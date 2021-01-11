from random import randrange


class ArrayGenerator:
    @staticmethod
    def generate_ordered_array(n):
        return list(range(n))

    @staticmethod
    def generate_random_array(n, bound):
        return [randrange(0, bound) for i in range(n)]


if __name__ == '__main__':
    print(ArrayGenerator.generate_random_array(10, 1))
