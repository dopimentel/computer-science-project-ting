from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self._queue = []

    def __len__(self):
        return len(self._queue)

    def enqueue(self, value):
        self._queue.append(value)

    def dequeue(self):
        return self._queue.pop(0)

    def search(self, index):
        if index < 0 or index >= len(self._queue):
            raise IndexError("Índice Inválido ou Inexistente")
        return self._queue[index]

    def index_of(self, value):
        try:
            return self._queue.index(value)
        except ValueError:
            return -1


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print(queue.search(0))
    print(len(queue))
