# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        q = collections.deque([(root, 0)])
        res = 0
        while q:
            res = max(res, q[-1][1] - q[0][1])
            for _ in range(len(q)):
                current, d = q.popleft()
                if current.left:
                    q.append((current.left, 2*d))
                if current.right:
                    q.append((current.right, 2*d+1))
        return res + 1
        
        
        