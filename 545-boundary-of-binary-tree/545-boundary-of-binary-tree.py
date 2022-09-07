# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        
        res = [root.val]
        def inn(node):
            if not node:
                return 
            inn(node.left)
            if node != root and not node.left and not node.right:
                res.append(node.val)
            inn(node.right)
        
        def left(node):
            if not node or not node.left and not node.right:
                return
            if node.right:
                left(node.right)
            else:
                left(node.left)
            res.append(node.val)
                
        def top(node):
                if not node or not node.left and not node.right:
                    return
                res.append(node.val)
                if node.left:
                    top(node.left)
                else:
                    top(node.right)
                
        top(root.left)
        inn(root)
        left(root.right)
        return res