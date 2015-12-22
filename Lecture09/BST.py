from BinaryTree import BinaryTree, BTNode

def is_leaf(node):
    return node._left is None and node._right is None

def remove_child(parent, child):
    if child == parent._left:
        parent._left = None
    elif child == parent._right:
        parent._right = None
    else:
        return

def get_inorder_successor(node):
    current = node._right
    while True:
        if current._left == None:
            return current
        current = current._left

class BST(BinaryTree):

    def find_node(self, item):
        current = self._root
        while current is not None:
            if current._item == item:
                return current
            elif current._item < item:
                current = current._right
            else:
                current = current._left
        return None

    def find_parent_of(self, node):
        if node == self._root:
            return None
        current = self._root
        while True:
            if current._left == node or current._right == node:
                return current
            elif current._item < node._item:
                current = current._right
            else:
                current = current._left        
    def delete(self, item):
        self.delete_node(self.find_node(item))
                
    def delete_node(self, node):
        if node is None:
            return

        #Case 1 (Leaf)
        if is_leaf(node):
            remove_child(self.find_parent_of(node),node)
        #Case 2a (Has only right child)
        elif node._left == None:
            if node == self._root:
                self._root = node._right
            else:
                parent = self.find_parent_of(node)
                if parent._left == node:
                    parent._left = node._right
                else:
                    parent._right = node._right
        #Case 2b (has only left child)
        elif node._right == None:
            if node == self._root:
                self._root = node._left
            else:
                parent = self.find_parent_of(node)
                if parent._left == node:
                    parent._left = node._left
                else:
                    parent._right = node._left
        #Case 3 (internal node -- both children)
        else:
            ios = get_inorder_successor(node)
            temp = ios._item
            self.delete_node(ios)
            node._item = temp
        
    def insert(self, item ):
        current = self._root
        if current is None:
            self._root = BTNode(item, None, None)
            return
        while True:
            if current._item < item:
                if current._right is None:
                    current._right = BTNode(item,None,None)
                    return
                current = current._right
            else:
                if current._left is None:
                    current._left = BTNode(item,None,None)
                    return
                current = current._left


bst = BST()
for i in range(10): bst.insert(randint(0,100))
bst.inorder(print)
