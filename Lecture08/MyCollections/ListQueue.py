from LinkedList import LinkedList


class ListQueue:

    def __init__(self):
        self._data = LinkedList()

    def enqueue(self, value):
        self._data.insertAtTail(value)

    def dequeue(self):
        return self._data.pop_head()

    def is_empty(self):
        return (self._data.size() == 0)

    def size(self):
        self._data.size()
