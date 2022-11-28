# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        d = 0
        
        p = root
        
        while p.left:
            p = p.left
            d += 1
        
        print(d)
        def check(index, node):
            l = 0
            r = 2**d - 1
            
            
            for _ in range(d):
                mid = (l+r) // 2
                if mid >= index:
                    node = node.left
                    r = mid
                else:
                    node = node.right
                    l = mid + 1
            return node != None
        
        
        left = 0
        right = 2**d - 1
        
        while left <= right:
            mid = (left+right) // 2
            if check(mid, root):
                left = mid + 1
            else:
                right = mid - 1
        
        return 2**d - 1 + left
        