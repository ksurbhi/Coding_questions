class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None
    
class Tree:
    def createNode(self, data):
        Node(data)
    def insert(self,node, data):
        if node is None:
            node.left = self.createNode(data)
        if data< node.data:
            node.right = self.insert(node.left, data)
        else:
            self.insert(node.right, data)
        return node

    def depth(self, root):
        if root is None:
            return 0
        retrun 1 + max(self.depth(root.left), self.depth(root.right))

    def height(self, root):
        if root is None:
            return -1
        retrun 1 + max(self.height(root.left), self.height(root.right))

tree = Tree()

root = tree.createNode(5)
tree.insert_data(root, 2)
tree.insert_data(root, 7)
tree.insert_data(root, 8)
tree.insert_data(root, 3)
tree.insert_data(root, 20)
tree.insert_data(root, 15)
tree.insert_data(root, 12)
tree.insert_data(root, 6)
tree.insert_data(root, 10)

res = tree.height(root)
print(res)
