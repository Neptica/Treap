# Returns None if root_node is the root of a valid BST.
# If a BST violation occurs, the node causing the violation is returned. Such a
# node may be one of three things:
# 1. A node in the left subtree of an ancestor with a lesser key
# 2. A node in the right subtree of an ancestor with a greater key
# 3. A node with the left or right attribute referencing an ancestor
def check_bst_validity(root_node):
    # Make a node stack
    nodes = [root_node]

    # Check for loops first
    distinct_set = set()
    while len(nodes) > 0:
        node = nodes.pop()
        if node is not None:
            # Add the node to the set of distinct nodes visited
            distinct_set.add(node)
            #
            # If either of the node's children is in distinct_set then the node
            # is invalid due to either:
            #   referencing an ancestor and thus causing a loop in the tree
            #   or
            #   referencing a non-ancestor node from another part of the tree
            #   and thus making a node have two parent nodes.

            # This lab's test cases only test the former and not the latter.
            """ your code here"""
            if node.left in distinct_set or node.right in distinct_set:
                return node
            # Append children to the list
            """ your code here"""
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)

    # Check for key violations second
    nodes = [root_node]
    while len(nodes) > 0:
        node = nodes.pop()
        if node is not None:
            # Check for key-related violations; return bad_node
            # use Python anonymous function; the lambda keyword is used to create anonymous functions.
            # lambda other_node: other_node.key <= node.key
            """your code lines go here"""
            left_check = lambda child_node: child_node.key > node.key
            right_check = lambda child_node: child_node.key < node.key
            # Append children to the list
            if node.left:
                maybe_bad = find_violator(node.left, left_check)
                if maybe_bad:
                    return maybe_bad
                nodes.append(node.left)
            if node.right:
                maybe_bad = find_violator(node.right, right_check)
                if maybe_bad:
                    return maybe_bad
                nodes.append(node.right)
            """ your code here"""

    # Arriving here implies that no violations were found
    return None


# Visits all nodes in the subtree and returns the first encountered node that
# doesn't satisfy the predicate. Returns None if all nodes satisfy.
def find_violator(subtree_root, predicate):
    # Special case for subtree_root being None
    """your code here"""
    if not subtree_root:
        return None

    # Test each node with the predicate. If the predicate returns False for any
    # node, then return that node.
    nodes = [subtree_root]
    """ your code here"""
    while len(nodes) > 0:
        curr = nodes.pop()
        if predicate(curr):
            return curr
        if curr.left:
            nodes.append(curr.left)
        if curr.right:
            nodes.append(curr.right)

    return None
