#1  Method to Find the Maximum Value in the BST
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    def find_max(self):
        if self.root is None:
            return None
        current = self.root
        while current.right:
            current = current.right
        return current.value
    
#2 Method to Count the Total Number of Nodes in the BST
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    def find_max(self):
        if self.root is None:
            return None
        current = self.root
        while current.right:
            current = current.right
        return current.value
    
    #Method to Count the Total Number of Nodes in the BST

    def count_nodes(self):
        return self._count_nodes_recursive(self.root)

    def _count_nodes_recursive(self, node):
        if node is None:
            return 0
        return 1 + self._count_nodes_recursive(node.left) + self._count_nodes_recursive(node.right)


bst = BST()
values = [10, 5, 15, 3, 7, 13, 18]
for v in values:
    bst.insert(v)

#3 Level-Order Traversal (Breadth-First Search) for the BST
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    def find_max(self):
        if self.root is None:
            return None
        current = self.root
        while current.right:
            current = current.right
        return current.value
    
    #Method to Count the Total Number of Nodes in the BST

    def count_nodes(self):
        return self._count_nodes_recursive(self.root)

    def _count_nodes_recursive(self, node):
        if node is None:
            return 0
        return 1 + self._count_nodes_recursive(node.left) + self._count_nodes_recursive(node.right)
    
    #Level-Order Traversal (Breadth-First Search) for the BST

    def level_order_traversal(self):
        if self.root is None:
            return []
        
        result = []
        queue = [self.root]
        
        while queue:
            current = queue.pop(0)
            result.append(current.value)
            
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        
        return result
    
bst = BST()
values = [10, 5, 15, 3, 7, 13, 18]
for v in values:
    bst.insert(v)

#4 Method to Find the Height of the BST
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    def find_max(self):
        if self.root is None:
            return None
        current = self.root
        while current.right:
            current = current.right
        return current.value
    
    #Method to Count the Total Number of Nodes in the BST

    def count_nodes(self):
        return self._count_nodes_recursive(self.root)

    def _count_nodes_recursive(self, node):
        if node is None:
            return 0
        return 1 + self._count_nodes_recursive(node.left) + self._count_nodes_recursive(node.right)
    
    #Level-Order Traversal (Breadth-First Search) for the BST

    def level_order_traversal(self):
        if self.root is None:
            return []
        
        result = []
        queue = [self.root]
        
        while queue:
            current = queue.pop(0)
            result.append(current.value)
            
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        
        return result
    
    #Method to Find the Height of the BST

    def find_height(self):
        return self._find_height_recursive(self.root)

    def _find_height_recursive(self, node):
        if node is None:
            return -1
        left_height = self._find_height_recursive(node.left)
        right_height = self._find_height_recursive(node.right)
        return 1 + max(left_height, right_height)

bst = BST()
values = [10, 5, 15, 3, 7, 13, 18]
for v in values:
    bst.insert(v)

#5 Method to Check if the Tree is a Valid BST
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    def find_max(self):
        if self.root is None:
            return None
        current = self.root
        while current.right:
            current = current.right
        return current.value
    
    #Method to Count the Total Number of Nodes in the BST

    def count_nodes(self):
        return self._count_nodes_recursive(self.root)

    def _count_nodes_recursive(self, node):
        if node is None:
            return 0
        return 1 + self._count_nodes_recursive(node.left) + self._count_nodes_recursive(node.right)
    
    #Level-Order Traversal (Breadth-First Search) for the BST

    def level_order_traversal(self):
        if self.root is None:
            return []
        
        result = []
        queue = [self.root]
        
        while queue:
            current = queue.pop(0)
            result.append(current.value)
            
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        
        return result
    
    #Method to Find the Height of the BST

    def find_height(self):
        return self._find_height_recursive(self.root)

    def _find_height_recursive(self, node):
        if node is None:
            return -1
        left_height = self._find_height_recursive(node.left)
        right_height = self._find_height_recursive(node.right)
        return 1 + max(left_height, right_height)

    #Method to Check if the Tree is a Valid BST
    def is_valid_bst(self):
        return self._is_valid_bst_recursive(self.root, float('-inf'), float('inf'))

    def _is_valid_bst_recursive(self, node, min_val, max_val):
        if node is None:
            return True
        if not (min_val < node.value < max_val):
            return False
        return (self._is_valid_bst_recursive(node.left, min_val, node.value) and
                self._is_valid_bst_recursive(node.right, node.value, max_val))

bst = BST()
values = [10, 5, 15, 3, 7, 13, 18]
for v in values:
    bst.insert(v)

print("Max Value:", bst.find_max())
print("Total Nodes:", bst.count_nodes())
print("Level Order Traversal:", bst.level_order_traversal())
print("Height of BST:", bst.find_height())
print("Is Valid BST:", bst.is_valid_bst())