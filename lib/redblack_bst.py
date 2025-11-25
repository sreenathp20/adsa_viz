class RedBlackTreeNode:

    def __init__(self, key, color='red', left=None, right=None, parent=None):
        self.key = key
        self.color = color  # 'red' or 'black'
        self.left = left
        self.right = right
        self.parent = parent

    def __repr__(self):
        return f'Node({self.key}, {self.color})'
    
    def is_red(self):
        return self.color == 'red'
    
    def is_black(self):
        return self.color == 'black'
    
    def set_red(self):
        self.color = 'red'  

    def set_black(self):
        self.color = 'black'


class RBT:

    def __init__(self):
        self.NIL_LEAF = RedBlackTreeNode(key=None, color='black')
        self.root = self.NIL_LEAF

    def insert(self, key):
        if self.root == self.NIL_LEAF:
            self.root = RedBlackTreeNode(key, color='black', left=self.NIL_LEAF, right=self.NIL_LEAF)
            return self.root
        else:
            node = RedBlackTreeNode(key)
            node.left = self.NIL_LEAF
            node.right = self.NIL_LEAF
            current = self.root
            while current != self.NIL_LEAF:
                if node.key < current.key:
                    current = current.left
                elif node.key > current.key:
                    current = current.right
                else:
                    return current  # Key already exists
            node.parent = current
            if node.key < current.key:
                current.left = node
            else:
                current.right = node
            node.set_red()
            self._fix_insert(node)
            return node
        
    def _fix_insert(self, node):
        if node.parent.color == 'black':
            return
        parent = node.parent
        grandparent = parent.parent
        if grandparent.left != self.NIL_LEAF and grandparent.left == parent:
            uncle = grandparent.right
        if grandparent.right != self.NIL_LEAF and grandparent.right == parent:
            uncle = grandparent.left  # parent is right child
            if parent.right != self.NIL_LEAF and node == parent.right:
                self.left_rotate(parent)
        if uncle == self.NIL_LEAF or uncle.is_black():
            if parent.left != self.NIL_LEAF and node.key == parent.left.key:
                if grandparent.left != self.NIL_LEAF and parent.key == grandparent.left.key:
                    pass

    def left_rotate(self, x):
        parent = x.parent
        y = x.right
        if parent != self.NIL_LEAF and parent.parent.left == parent:
            parent.parent.left = x
        if parent != self.NIL_LEAF and parent.parent.right == parent:
            parent.parent.right = x
        x.parent = parent.parent
        parent.right = x.left
        if x.left != self.NIL_LEAF:
            x.left.parent = parent
        x.left = parent
        parent.parent = x


class RedBlackTree:

    def __init__(self):
        self.NIL_LEAF = RedBlackTreeNode(key=None, color='black')
        self.root = self.NIL_LEAF

    def insert(self, key):
        new_node = RedBlackTreeNode(key)
        new_node.left = self.NIL_LEAF
        new_node.right = self.NIL_LEAF

        parent = None
        current = self.root

        while current != self.NIL_LEAF:
            parent = current
            if new_node.key < current.key:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent

        if parent is None:
            self.root = new_node
        elif new_node.key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

        new_node.set_red()
        self.fix_insert(new_node)

    def fix_insert(self, node):
        while node.parent and node.parent.is_red():
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.is_red():
                    node.parent.set_black()
                    uncle.set_black()
                    node.parent.parent.set_red()
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.set_black()
                    node.parent.parent.set_red()
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.is_red():
                    node.parent.set_black()
                    uncle.set_black()
                    node.parent.parent.set_red()
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.set_black()
                    node.parent.parent.set_red()
                    self.left_rotate(node.parent.parent)
        self.root.set_black()

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL_LEAF:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.NIL_LEAF:
            x.right.parent = y  
        x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x
    
    def inorder_traversal(self, node):
        if node != self.NIL_LEAF:
            self.inorder_traversal(node.left)
            print(node.key, end=' ')
            self.inorder_traversal(node.right)  

    def search(self, key):
        current = self.root
        while current != self.NIL_LEAF and key != current.key:
            if key < current.key:
                current = current.left
            else:
                current = current.right
        return current if current != self.NIL_LEAF else None

    def get_root(self):
        return self.root        

    
if __name__ == "__main__":
    rbt = RedBlackTree()
    keys = [20, 15, 25, 10, 5, 1, 30, 35, 40]
    keys = [10, 18, 7, 15, 16, 30, 25, 40, 60, 2, 1, 70]
    for key in keys:
        rbt.insert(key)

    print("Inorder Traversal of the Red-Black Tree:")
    rbt.inorder_traversal(rbt.get_root())
    print()

    search_key = 25
    result = rbt.search(search_key)
    if result:
        print(f"Key {search_key} found in the tree.")
    else:
        print(f"Key {search_key} not found in the tree.")
