class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class Tree:
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._add(value, self.root)

    def _add(self, value, node):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._add(value, node.left)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._add(value, node.right)

    def pre_order(self):
        if self.root is not None:
            self._pre_order(self.root)

    def _pre_order(self, node):
        if node is not None:
            print(node.value)
            self._pre_order(node.left)
            self._pre_order(node.right)
