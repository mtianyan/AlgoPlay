import random
import time
import ArrayStack
import LinkedListStack


def test_stack(q, count):
    start = time.time()
    for i in range(count):
        q.push(random.randint(1, 10))
    for i in range(count):
        q.pop()
    end = time.time()
    print(f'{q}, size: {count} : {end - start} s')


if __name__ == '__main__':
    op_count = 10000
    array_stack = ArrayStack.ArrayStack(op_count)
    test_stack(array_stack, op_count)

    link_stack = LinkedListStack.LinkedListStack()
    test_stack(link_stack, op_count)

    """
    Stack size: 0 capacity: 1 Array size: 0 capacity: 1 []<-top, size: 10000 : 13.747399806976318 s
    Stack top:->None, size: 10000 : 0.03333330154418945 s
    """