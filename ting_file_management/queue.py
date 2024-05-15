from ting_file_management.abstract_queue import AbstractQueue
from collections import deque


class Queue(AbstractQueue):
    def __init__(self):
        self.__data = deque()

    def __len__(self):
        return len(self.__data)

    def enqueue(self, value):
        self.__data.append(value)

    def dequeue(self):
        value = self.__data[0]
        self.__data.popleft()
        return value

    def search(self, index):
        valid_index = 0 <= index < self.__len__()
        if not isinstance(index, int) or not valid_index:
            raise IndexError("Índice Inválido ou Inexistente")
        value = self.__data[index]
        return value
