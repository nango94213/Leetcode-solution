"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        
        res = 0
        
        def dfs(node):
            
            nonlocal res
            
            if not node:
                return 0
            
            all_child = []
    
            for child in node.children:
                all_child.append(dfs(child))
            
 
        
            all_child.sort()
            
            if len(all_child) >= 2:
                res = max(res, all_child[-1] + all_child[-2])
                return all_child[-1] + 1
            elif len(all_child) == 1:
                res = max(res, all_child[0])
                return all_child[0] + 1
            else:
                return 1
        
        dfs(root)
        
        return res
            
                
                