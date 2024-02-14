# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def in_order(self, root, values):
            if root is not None:
                left_val = self.in_order(root.left,values)
                values.append(root.val)
                right_val = self.in_order(root.right,values)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        values = []
        self.in_order(root, values)
        # print(values)
        for i in range(len(values)-1):
            if values[i] >= values[i+1]:
                return False
        return True
        
