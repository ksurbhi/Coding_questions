def topOrderView(self, root):
        dict = {}
        queue = deque()
        hd = 0
        if root:
            queue.append((root,hd))
        while len(queue) != 0:
            root, hd = queue.popleft()
            if hd not in dict:
                dict[hd] = root.data
            if root.left:
                queue.append((root.left,hd-1))
            if root.right:
                queue.append((root.right,hd+1))
        return sorted(dict.values())



# # Driver code
tree = Tree()
root = tree.createNode(5)
