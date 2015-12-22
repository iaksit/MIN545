class ListNode:
    def __init__(self, value, next):
        self._value = value
        self._next = next

    def get_value(self):
        return self._value
    def set_value(self,value):
        self._value = value
    def next(self):
        return self._next
    def set_next(self,next):
        self._next = next

class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def size(self):
        return self._size

    def insertAtHead(self,value):
        self._head = ListNode(value, self._head)
        self._size += 1

    def insertAtTail(self, value):
        if self._head == None:
            self._head = ListNode(value, self._head)
            self._tail = self._head
        else:
            temp = ListNode(value, None)
            self._tail.set_next(temp)
            self._tail = temp
        self._size += 1
        
    def printList(self):
        current = self._head
        while current != None:
            print(current.get_value())
            current = current.next()
            
    def get_node(self,idx):
        "Get the ith node"
        if (idx > self._size-1):
            return None
        current = self._head
        i = 0
        while i < idx:
            current = current.next()
            i +=1
        return current

    def pop_head(self):
        if self._head != None:
            temp = self._head
            self._head = temp.next()
            self._size -= 1
            return temp.get_value()
        else:
            return None

    def insert_before(self, value, idx):
        if idx >= self._size:
            raise IndexError("Really?!!")
        if idx == 0:
            self.insertAtHead(value)
        else:
            preceeding_node = self.get_node(idx-1)
            temp = ListNode(value, preceeding_node.next())
            preceeding_node.set_next(temp)
            self._size += 1
            
    def __contains__(self, target):
        return self.recursive_contains(self._head, target)

    def recursive_contains(self, node, target):
        if node == None:
            return False
        if node.get_value() == target:
            return True
        return self.recursive_contains(node.next(), target)

    def is_circular(self):
        turtle = self._head
        rabbit = self._head

        while turtle != None or rabbit != None:
            turtle = turtle.next()
            if turtle == None:
                return False
            rabbit = rabbit.next()
            if rabbit == None:
                return False
            rabbit = rabbit.next()
            if rabbit == None:
                return False
            if rabbit == turtle:
                return True

        return False


if __name__ == '__main__':   
    mylist = LinkedList()
    mylist.insertAtHead("Zafer")
    mylist.insertAtHead("Yasemin")
    mylist.insertAtHead("Kaan")
    mylist.insertAtHead("Feride")
    mylist.insertAtHead("Deniz")
    mylist.insertAtHead("Cengiz")
    mylist.insertAtHead("Bulent")
    mylist.insertAtHead("Ayse")
    mylist.printList()
