# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        
        def dfs(pool, path, current):
            if pool:
                
                if not pool.left and not pool.right and current == pool.val:
                    path.append(pool.val)
                    res.append(path)
                    return
                
                dfs(pool.left, path + [pool.val], current - pool.val)
                dfs(pool.right, path + [pool.val], current - pool.val)
        
        dfs(root, [], targetSum)
        
        return res