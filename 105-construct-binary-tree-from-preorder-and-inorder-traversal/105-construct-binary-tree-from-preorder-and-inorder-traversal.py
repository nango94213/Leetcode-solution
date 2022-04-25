# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        dic = {}
        
        for i, v in enumerate(inorder):
            dic[v] = i
        
        
        def dfs(sub):
            
            if sub:
                current =  preorder.pop(0)
            
                index = dic[current] - dic[sub[0]]
            
                root = TreeNode(current)
            
                root.left = dfs(sub[:index])
                root.right = dfs(sub[index+1:])
            
                return root
        
        return dfs(inorder)