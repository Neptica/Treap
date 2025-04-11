from check_validity import check_bst_validity


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
                        node.parent = current_node
                        current_node = None
                    else:
                        current_node = current_node.left
                elif node.key > current_node.key:
                    if current_node.right is None:
                        current_node.right = node
                        node.parent = current_node
                        current_node = None
                    else:
                        current_node = current_node.right
                else:
                    raise ValueError(
                        f"'{node.key}' cannot be inserted. Value already exists in tree."
                    )

        # Key always inserted
        self.count += 1
        self.percolate_up(node)

    def remove(self, key):
        current_node = self.root

        while current_node:

            if current_node.key == key:
                current_node.priority = float("-inf")
                break
            elif key > current_node.key:
                current_node = current_node.right
            else:
                current_node = current_node.left

        if current_node:
            self.percolate_down(current_node)
            # Disconnect the node from the tree after making it a leaf node
            if current_node.parent:
                if current_node.parent.right == current_node:
                    current_node.parent.right = None
                else:
                    current_node.parent.left = None
            else:
                # Node is root and leaf node, thus the only node in the tree
                self.root = None

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

    def percolate_up(self, node):
        parent = node.parent
        while node and parent:
            if parent.priority < node.priority:
                if parent.right == node:
                    node = self.rotate_left(parent)
                else:
                    node = self.rotate_right(parent)
                parent = node.parent
            else:
                break

    def percolate_down(self, node):
        while node.left or node.right:
            if node.left and node.right:
                if node.left.priority < node.right.priority:
                    self.rotate_left(node)
                else:
                    self.rotate_right(node)
            elif node.left:
                self.rotate_right(node)
            else:
                self.rotate_left(node)

    def rotate_right(self, node):
        parent = node.parent
        new_parent = node.left

        # Make old n1 point to new n1 (Parent)
        node.parent = new_parent

        # Update carryover child if not null
        node.left = new_parent.right
        if new_parent.right:
            new_parent.right.parent = node

        # Make new n1 point to old n1 as n3 (child)
        new_parent.right = node

        # Update common ancester (n1's parent) node to point to new n1 node (previously n2)
        new_parent.parent = parent
        if parent:
            if parent.right == node:
                parent.right = new_parent
            else:
                parent.left = new_parent
        else:
            self.root = new_parent

        bad_node = check_bst_validity(self.root)
        if bad_node:
            raise AttributeError("Bad pointer", bad_node)
        return new_parent

    def rotate_left(self, node):
        parent = node.parent
        new_parent = node.right

        # Make old n1 point to new n1 (Parent)
        node.parent = new_parent

        # Update carryover child if not null
        node.right = new_parent.left
        if new_parent.left:
            new_parent.left.parent = node

        # Make new n1 point to old n1 as n2 (child)
        new_parent.left = node

        # Update common ancester (n1's parent) node to point to new n1 node (previously n3)
        new_parent.parent = parent
        if parent:
            if parent.right == node:
                parent.right = new_parent
            else:
                parent.left = new_parent
        else:
            self.root = new_parent

        bad_node = check_bst_validity(self.root)
        if bad_node:
            raise AttributeError("Bad pointer", bad_node)
        return new_parent
