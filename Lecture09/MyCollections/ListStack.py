from MyCollections.LinkedList import LinkedList

class ListStack:

    def __init__(self):
        self._data = LinkedList()

    def push(self, value):
        self._data.insertAtHead(value)
        
    def pop(self):
        return self._data.pop_head()

    def is_empty(self):
        return (self._data.size() == 0)

    def peek(self):
    	return self._data._head.get_value()

        
