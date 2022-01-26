class TreeNode:  # Remember, it's a recursive data structure
    def __init__(self, data):
        self.data = data
        self.children = []  # and so all the children will be an instance of treenode itself
        self.parent = None

    def get_level(self):  # cute method to find number of ancestors you have and use it
        level = 0
        p = self.parent
        while p:  # while you have a parent, do the following.
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3  # print times 3 spaces per level to make stuff pretty
        prefix = spaces + "|-->" if self.parent else ""
        print(prefix + self.data)
        if self.children:  # checking if we have children and it's not a leaf node aka len > 0
            for child in self.children:
                child.print_tree()  # recursively printing the data

    def add_child(self, child):  # important
        child.parent = self  # the child's parent will be the instance of the class itself
        self.children.append(child)

def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Google Pixel"))
    cellphone.add_child(TreeNode("Vivo"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    root.print_tree()

if __name__ == '__main__':
    build_product_tree()
