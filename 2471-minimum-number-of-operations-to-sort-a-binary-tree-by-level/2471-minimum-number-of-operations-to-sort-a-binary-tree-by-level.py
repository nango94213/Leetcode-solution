# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        q = collections.deque([root])
        
        res = 0
        
        while q:
            level = []
            for _ in range(len(q)):
                current = q.popleft()
                level.append(current.val)
                
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)
            
            count = 0
            new = sorted(level)
            dic = {}
            for i, v in enumerate(level):
                dic[v] = i
            for i in range(len(level)):
                if level[i] != new[i]:
                    count += 1
                    index = dic[new[i]]
                    dic[new[i]] = i
                    dic[level[i]] = index
                    level[i], level[index] = level[index], level[i]

            res += count
        return res
        