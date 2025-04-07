class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.dataType = None
        self.count = 0

    def insert(self, node):

        if not self.dataType:
            self.dataType = type(node.key)
        elif self.dataType != type(node.key):
            raise TypeError(
                f"Value '{node.key}' cannot be inserted. Data is not of type {self.dataType}."
            )

        if self.root is None:
            self.root = node
        else:
            current_node = self.root
            while current_node is not None:
                if node.key < current_node.key:
                    if current_node.left is None:
                        current_node.left = node
                        current_node = None
                    else:
                        current_node = current_node.left
                elif node.key > current_node.key:
                    if current_node.right is None:
                        current_node.right = node
                        current_node = None
                    else:
                        current_node = current_node.right
                else:
                    raise ValueError(
                        f"'{node.key}' cannot be inserted. Value already exists in tree."
                    )

        # Key always inserted
        self.count += 1

    def remove(self, key):
        parent = None
        current_node = self.root

        while current_node is not None:

            if current_node.key == key:
                # Key found, removal in progress
                self.count -= 1
                if current_node.left is None and current_node.right is None:
                    if parent is None:
                        self.root = None
                    elif parent.left is current_node:
                        parent.left = None
                    else:
                        parent.right = None
                    return
                elif current_node.left is not None and current_node.right is None:
                    if parent is None:
                        self.root = current_node.left
                    elif parent.left is current_node:
                        parent.left = current_node.left
                    else:
                        parent.right = current_node.left
                    return
                elif current_node.left is None and current_node.right is not None:
                    if parent is None:
                        self.root = current_node.right
                    elif parent.left is current_node:
                        parent.left = current_node.right
                    else:
                        parent.right = current_node.right
                    return
                else:
                    successor = current_node.right
                    while successor.left is not None:
                        successor = successor.left
                    current_node.key = successor.key
                    parent = current_node
                    current_node = current_node.right
                    key = parent.key
                    self.count += 1
            elif current_node.key < key:
                parent = current_node
                current_node = current_node.right
            else:
                parent = current_node
                current_node = current_node.left

        return

    def search(self, desired_key):
        current_node = self.root

        while current_node is not None:
            if current_node.key == desired_key:
                return current_node
            elif desired_key < current_node.key:
                current_node = current_node.left
            else:
                current_node = current_node.right

        return None

    def count_nodes(self):
        return self.count

    def height(self, root):
        if not root:
            return -1

        left = self.height(root.left)
        right = self.height(root.right)
        return 1 + max(left, right)
