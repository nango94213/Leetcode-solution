# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        
        dic = {}
        
        def dfs(node, parent):
            
            if not node:
                return
            
            dic[node.val] = parent
            
            dfs(node.left, node.val)
            dfs(node.right, node.val)
        
        dfs(root, -1)
        
        p_parent = set()
        
        tmp = p
        while tmp != -1:
            p_parent.add(tmp)
            
            tmp = dic[tmp]
        
        
        count2 = 0
        while q not in p_parent:
            q = dic[q]
            count2 += 1
        
        
        count1 = 0
        
        while p != q:
            count1 += 1
            p = dic[p]
        
        return count1 + count2
        
       
            
            
        
        
        
            
            
        