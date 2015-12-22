class ArrayQueue:

    DEFAULT_CAPACITY = 10
    
    def __init__(self):        
        self._data = [ None for i in range(ArrayQueue.DEFAULT_CAPACITY)]
        self._front = 0
        self._back = 0
        self._size = 0

    def size(self):
        return self._size()
    
    def is_empty(self):
        # return self._size == 0
        return self._front == self._back

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            temp = self._data[self._front]
            self._data[self._front] = None
            self._front = (self._front + 1) % len(self._data)
            self._size -= 1
            return temp

    def enqueue(self, value):
        if (self._back + 1) % len(self._data) == self._front: ## need to resize
            self.resize()

        self._data[self._back] = value
        self._back = (self._back + 1) % len(self._data)
        self._size += 1

    def resize(self):
        new_data = [None for i in range(len(self._data * 2))]
        i = 0
        while not self.is_empty():
            new_data[i] = self.dequeue()
            i += 1
        self._front = 0
        self._back = i
        self._data = new_data
        
            
