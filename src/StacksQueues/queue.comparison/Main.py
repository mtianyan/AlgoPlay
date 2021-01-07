import random
import time
import ArrayQueue
import LoopQueue


def test_queue(q, count):
    start = time.time()
    for i in range(count):
        q.enqueue(random.randint(1, 10))
    for i in range(count):
        q.dequeue()
    end = time.time()
    print(f'{q}, size: {count} : {end - start} s')


if __name__ == '__main__':
    op_count = 10000
    loopQueue = LoopQueue.LoopQueue(op_count)
    test_queue(loopQueue, op_count)

    arrayQueue = ArrayQueue.ArrayQueue(op_count)
    test_queue(arrayQueue, op_count)

    """
    size: 0 capacity: 0 front: 0 tail: 10000 loop queue->[], size: 10000 : 0.13201308250427246 s
    size: 0 capacity: 1 queue->Array size: 0 capacity: 1 [], size: 10000 : 24.28545308113098 s
    """
