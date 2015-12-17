class BTNode:
    def __init__(self,item,left=None,right=None):
        self._item = item
        self._left = left
        self._right = right

    def get_as_list(self):
        return (self._item, self._left, self._right)

## Data centric:

sample_tree = [1, [2, None, [4, [5, None, None], None]], [3, None, None]]

class BinaryTree:
    def __init__(self, initial=None):
        self._root = None
        if initial is not None:
            self._root = BinaryTree.build_tree(initial)

    def build_tree(node):
        #Base case
        if node is None:
            return None
        item, left, right = node
        return BTNode(item, BinaryTree.build_tree(left), BinaryTree.build_tree(right))

    def inorder_dfs(node,func):
        if node is None:
            return
        item, left, right = node.get_as_list()
        BinaryTree.inorder_dfs(left,func)
        func(item)
        BinaryTree.inorder_dfs(right,func)
    
    def inorder(self, func):
        BinaryTree.inorder_dfs(self._root, func)


    def postorder_dfs(node,func):
        if node is None:
            return
        item, left, right = node.get_as_list()
        BinaryTree.postorder_dfs(left,func)
        BinaryTree.postorder_dfs(right,func)
        func(item)
        
    
    def postorder(self, func):
        BinaryTree.postorder_dfs(self._root, func)

    def preorder_dfs(node,func):
        if node is None:
            return
        item, left, right = node.get_as_list()
        func(item)
        BinaryTree.preorder_dfs(left,func)
        BinaryTree.preorder_dfs(right,func)
    
    def preorder(self, func):
        BinaryTree.preorder_dfs(self._root, func)
        

    
mybt = BinaryTree(sample_tree)
