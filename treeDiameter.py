def treeDiameter(self, root):
        res =[0]
        def dfs(root):
            if root is None:
                return -1
            lh = dfs(root.left)
            rh = dfs(root.right)
            dia = lh + rh + 2
            res[0] = max(res[0], dia)
            return 1 + max(lh, rh)
        dfs(root)
        return res[0]
