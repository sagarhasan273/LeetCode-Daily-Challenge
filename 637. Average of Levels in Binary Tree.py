# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        hashMap = {}
        hashMap_l = {}
        
        def dfs(root, depth):
            if not root:
                return root
            if depth not in hashMap:
                hashMap[depth] = 0
                hashMap_l[depth] = 0
            hashMap[depth] += root.val
            hashMap_l[depth] += 1
            dfs(root.left, depth+1)
            dfs(root.right, depth+1)
        
        res = []
        dfs(root, 1)
        
        for i in hashMap.keys():
            print(hashMap[i])
            res.append(hashMap[i] / hashMap_l[i])
        
        return res