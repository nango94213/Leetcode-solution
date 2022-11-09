# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        dic = {}
        
        for i, v in enumerate(inorder):
            dic[v] = i
        
        
        def dfs(sub):
            if not sub:
                return None
            if sub and postorder:
                current = postorder.pop()
                index = dic[current] - dic[sub[0]]
                
                new = TreeNode(current)
                
                new.right = dfs(sub[index+1:])
                new.left = dfs(sub[:index])
                
                
                return new
            
        return dfs(inorder)