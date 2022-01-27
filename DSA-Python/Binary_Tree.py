class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):  # whatever object is passed in root, we're setting it as our root by making it a node
        self.root = Node(root)

        # below checking out 3 diff depth first search traversal ways
    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(tree.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(tree.root, "")

        else:
            print("Traversal type " + str(traversal_type) + " is not supported.")
            return False

    def preorder_print(self, start, traversal): # start is the node we start from and will get updated, traversal is the string we'll display in the end
        """Root->Left->Right"""  # mnemonic Ro-le-ri, rhymes with pre! pre has r, so starts with root, r
        if start:
            traversal += (str(start.value) + "-")  # just like the order, we start from root
            traversal = self.preorder_print(start.left, traversal)  # then recursively look for and print all left nodes in each level
            traversal = self.preorder_print(start.right, traversal)  # # then recursively look for and print all right nodes in each level
        return traversal

    def inorder_print(self, start, traversal):
        """Left->Root->Right"""  
        if start:
            traversal = self.inorder_print(start.left, traversal)  # just like the order, first print left subtree, their rights then
            traversal += (str(start.value) + "-")  # and then print the root after moving back up
            traversal = self.inorder_print(start.right, traversal)  # followed by right subtree
        return traversal

    def postorder_print(self, start, traversal):
        """Left->Right->Root"""  # mnemonic le-ri-roo, rhymes with postoo!
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal

# 1-2-4-5-3-6-7-
# 4-2-5-1-6-3-7
# 4-2-5-6-3-7-1
#               1
#           /       \
#          2          3
#         /  \      /   \
#        4    5     6   7

# Set up tree:
tree = BinaryTree(1)  # we're setting root node to 1, from this all children node will branch
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

#print(tree.print_tree("preorder"))
#print(tree.print_tree("inorder"))
print(tree.print_tree("postorder"))