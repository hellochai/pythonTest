class MyStack(object):
    def __init__(self):
        self.top = 0
        self.content = []

    def push(self, var):
        self.content.append(var)

    def getMin(self):
        min(self.content)

    def pop(self):
        self.content.pop()

class Node(object):
    def __init__(self, data=-1):
        self.data = data
        self.left  = None
        self.right  = None

class Tree(object):
    def iner_tree(self, tree: Node):
        tree_list = []
        if not (tree.left or tree.right):
            return None
        if tree.left:
            tree_list.append(tree.left)

