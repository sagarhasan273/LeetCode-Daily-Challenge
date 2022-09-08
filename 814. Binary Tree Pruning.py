class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        
        def contains_one(node):
            if not node:
                return 0
            
            left_one = contains_one(node.left)
            right_one = contains_one(node.right)
            
            if not left_one:
                node.left = None
            if not right_one:
                node.right = None
                
            return node.val or left_one or right_one
        
        return root if contains_one(root) else None