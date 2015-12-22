class ArrayStack:

    def __init__(self):
        self._data = []

    def push(self, value):
        self._data.append(value)

    def peek(self):
        return self._data[len(self._data)-1]
    
    def pop(self):
        try:
            return self._data.pop()
        except IndexError:
            return None
        
    def is_empty(self):
        return len(self._data) == 0
