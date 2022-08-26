# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class subTree:
    def __init__(self, largest, n, min, max):
            self.largest = largest
            self.n = n
            self.min = min
            self.max = max

class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        
        
        def dfs(node):
            
            if not node:
                return subTree(0, 0, float('inf'), -float('inf'))
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            if node.val > left.max and node.val < right.min:
                n = left.n + right.n + 1
            else:
                n = - float('inf')
            
            largest = max(left.largest, right.largest, n)
            
            return subTree(largest, n, min(left.min, node.val, right.min), max(right.max, node.val, left.max))
        
        return dfs(root).largest
        