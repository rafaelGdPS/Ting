from ting_file_management.abstract_queue import AbstractQueue
from collections import deque


class Queue(AbstractQueue):
    def __init__(self):
        self._data = deque()

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        value = self._data[0]
        self._data.popleft()
        return value

    def search(self, index):
        valid_index = 0 <= index < self.__len__()
        if not isinstance(index, int) or not valid_index:
            raise IndexError("Índice Inválido ou Inexistente")
        value = self._data[index]
        return value
