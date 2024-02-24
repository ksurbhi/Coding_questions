from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        result =[]
        if root:
            queue.append(root)
        while len(queue) != 0:
            value = []
            for i in range(len(queue)):
                root = queue.popleft()
                value.append(root.val)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            result.append(value)
        return [ele[-1] for ele in result]
        
