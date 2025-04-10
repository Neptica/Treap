class Node:
    def __init__(self, key, val):
        self.key = key
        self.priority = f"{val*100:.0f}"  # for value 0-99
        self.left = None
        self.right = None
        self.parent = None
