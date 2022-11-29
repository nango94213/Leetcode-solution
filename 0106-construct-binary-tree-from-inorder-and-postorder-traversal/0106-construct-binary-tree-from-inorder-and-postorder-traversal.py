# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        info = {}
        for i, v in enumerate(inorder):
            info[v] = i
        
        def dfs(s):
            if s:
                
                current = postorder.pop()
                index = info[current] - info[s[0]]
                root = TreeNode(current)
                
                root.right = dfs(s[index+1:])
                root.left = dfs(s[:index])
                
                return root
        
        return dfs(inorder)        