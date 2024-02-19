import pytest
from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():
    queue = PriorityQueue()
    assert queue.dequeue() is None

    queue.enqueue({"qtd_linhas": 5})
    queue.enqueue({"qtd_linhas": 6})
    queue.enqueue({"qtd_linhas": 4})
    assert len(queue) == 3
    assert queue.search(2) == {"qtd_linhas": 6}
    assert queue.search(0) == {"qtd_linhas": 4}
    assert queue.dequeue() == {"qtd_linhas": 4}
    assert queue.dequeue() == {"qtd_linhas": 5}
    assert queue.dequeue() == {"qtd_linhas": 6}
    assert len(queue) == 0

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        queue.enqueue({"qtd_linhas": 5})
        queue.enqueue({"qtd_linhas": 6})
        queue.search(5)

    assert len(queue) == 2
    assert queue.search(0) == {"qtd_linhas": 5}
    assert queue.search(1) == {"qtd_linhas": 6}

    assert queue.dequeue() == {"qtd_linhas": 5}
    assert queue.dequeue() == {"qtd_linhas": 6}
    assert len(queue) == 0
    assert queue.dequeue() is None
