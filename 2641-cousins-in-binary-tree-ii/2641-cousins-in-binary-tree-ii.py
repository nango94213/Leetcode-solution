# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = collections.deque()

        
        q.append([root, None])
        total = root.val
        while q:
            nextTotal = 0
            for _ in range(len(q)):
                currentOne, currentTwo = q.popleft()
                base = 0
                if currentOne:
                    base += currentOne.val
                if currentTwo:
                    base += currentTwo.val
                
                if currentOne:
                    currentOne.val = total - base
                    if currentOne.left:
                        nextTotal += currentOne.left.val
                    if currentOne.right:
                        nextTotal += currentOne.right.val
                    q.append([currentOne.left, currentOne.right])
                    
                if currentTwo:
                    currentTwo.val = total - base
                    if currentTwo.left:
                        nextTotal += currentTwo.left.val
                    if currentTwo.right:
                        nextTotal += currentTwo.right.val
                    q.append([currentTwo.left, currentTwo.right])
            total = nextTotal
        return root
