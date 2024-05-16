from ting_file_management.priority_queue import PriorityQueue
import pytest

file_1 = {
    "nome_do_arquivo": "arquivo_test_1.txt",
    "qtd_linhas": 7,
    "linhas_do_arquivo": [
        "testando",
        "lista com",
        "mais",
        "de",
        "cinco",
        "linhas",
        "no arquivo",
    ],
}
file_2 = {
    "nome_do_arquivo": "arquivo_test_2.txt",
    "qtd_linhas": 6,
    "linhas_do_arquivo": [
        "testanto",
        "seis",
        "linhas",
        "dentro",
        "do",
        "arquivo",
    ],
}
file_3 = {
    "nome_do_arquivo": "arquivo_test_3.txt",
    "qtd_linhas": 4,
    "linhas_do_arquivo": ["testando", "quatro", "linhas", "no arquivo"],
}
file_4 = {
    "nome_do_arquivo": "arquivo_test_4.txt",
    "qtd_linhas": 2,
    "linhas_do_arquivo": [
        "testando 2 linhas",
        "no arquivo",
    ],
}


def test_basic_priority_queueing():
    queue = PriorityQueue()
    assert len(queue) == 0

    queue.enqueue(file_1)
    queue.enqueue(file_3)

    assert len(queue) == 2
    assert len(queue.high_priority) == 1
    assert len(queue.regular_priority) == 1

    queue.enqueue(file_2)
    queue.enqueue(file_4)

    assert queue.search(1) == file_4

    assert len(queue) == 4
    assert len(queue.high_priority) == 2
    assert len(queue.regular_priority) == 2

    queue.dequeue()
    assert len(queue.high_priority) == 1
    assert len(queue.regular_priority) == 2

    with pytest.raises(IndexError):
        queue.search(7)
