# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        
        stack = collections.deque([])
        stack.append(root)
        visited = set()
        s = ''
        
        while stack:
            node = stack[-1]
            
            if node in visited:
                stack.pop()
                s += ")"
            else:
                visited.add(node)
                s += "(" + str(node.val)
                
                if not node.left and node.right:
                    s += "()"
                
                if node.right:
                    stack.append(node.right)
                    
                if node.left:
                    stack.append(node.left)
        
        return s[1:-1]