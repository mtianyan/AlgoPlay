import random
import time
import ArrayQueue
import LoopQueue
import LinkedListQueue

def test_queue(q, count):
    start = time.time()
    for i in range(count):
        q.enqueue(random.randint(1, 10))
    for i in range(count):
        q.dequeue()
    end = time.time()
    print(f'{q}, size: {count} : {end - start} s')


if __name__ == '__main__':
    op_count = 100000
    loopQueue = LoopQueue.LoopQueue(op_count)
    test_queue(loopQueue, op_count)

    # arrayQueue = ArrayQueue.ArrayQueue(op_count)
    # test_queue(arrayQueue, op_count)

    link_queue = LinkedListQueue.LinkedListQueue()
    test_queue(link_queue, op_count)

    """
    size: 0 capacity: 0 front: 0 tail: 10000 loop queue->[], size: 10000 : 0.13201308250427246 s
    size: 0 capacity: 1 queue->Array size: 0 capacity: 1 [], size: 10000 : 24.28545308113098 s
    queue: front:->tail, size: 10000 : 0.028388261795043945 s
    """

    """
    size: 0 capacity: 0 front: 0 tail: 100000 loop queue->[None], size: 100000 : 1.5835490226745605 s
    queue: front:->tail, size: 100000 : 0.3338940143585205 s
    """