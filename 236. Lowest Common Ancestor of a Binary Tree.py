class Solution:
    def __init__(self):
        self.ans = None

    def lowestCommonAncestor(self, root, p, q):
        
        def dfs(node):
            if not node:
                return False
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            mid = node == p or node == q
            
            if mid + left + right >= 2:
                self.ans = node
            
            return mid or left or right
        
        dfs(root)
        return self.ans
                