from ting_file_management.abstract_queue import AbstractQueue
from collections import deque


class Queue(AbstractQueue):
    def __init__(self):
        self._queue = deque()

    def __len__(self):
        return len(self._queue)

    def enqueue(self, value):
        self._queue.append(value)

    def dequeue(self):
        if len(self._queue) == 0:
            return None
        return self._queue.popleft()

    def search(self, index):
        if index < 0 or index >= len(self._queue):
            raise IndexError("Índice Inválido ou Inexistente")
        return self._queue[index]

    def index_of(self, value):
        try:
            return list(self._queue).index(value)
        except ValueError:
            return -1

    def queue(self):
        return list(self._queue)


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(2)
    queue.enqueue(3)

    print(queue.search(0))
    print(len(queue))
    print(queue.dequeue())
