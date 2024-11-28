import uuid

class TreeNode:
    """
    A node in a tree structure.
    Each node has a value, a unique identifier (uid), and links to its parent and children.
    """
    def __init__(self, value, parent=None):
        """
        Initializes a TreeNode with a value, an optional parent, and a unique ID.

        Args:
            value: The value to store in this node.
            parent (TreeNode, optional): The parent of this node. Default is None.
        """
        self.value = value
        self.parent = parent
        self.children = []  # Ensure children is unique to each instance
        self.uid = str(uuid.uuid4())  # Generate a unique identifier for this node

    def add_child(self, child):
        """
        Adds a child node to this node.

        Args:
            child (TreeNode): The child node to be added.
        """
        self.children.append(child)
        child.parent = self  # Set this node as the parent of the child

    def remove_child(self, child):
        """
        Removes a child node from this node.

        Args:
            child (TreeNode): The child node to be removed.
        """
        if child in self.children:
            self.children.remove(child)
            child.parent = None  # Disconnect the parent reference

    def get_paths(self):
        """
        Returns all paths from this node to its descendants.

        Returns:
            list: A list of paths, where each path is a list of node values.
        """
        if not self.children:  # Base case: no children
            return [[self]]

        paths = []
        for child in self.children:
            # For each child, prepend the current node's value to all descendant paths
            for path in child.get_paths():
                paths.append([self] + path)
        return paths
