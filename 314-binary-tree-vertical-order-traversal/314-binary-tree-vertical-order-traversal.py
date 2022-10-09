# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q = collections.deque([(root, 0)])
        
        dic = collections.defaultdict(list)
        
        while q:
            
            for _ in range(len(q)):
                
                current, x = q.popleft()
                
                dic[x].append(current.val)
                
                if current.left:
                    q.append((current.left, x-1))
                
                if current.right:
                    q.append((current.right, x+1))
        
        return [dic[key] for key in sorted(dic.keys())]
        
        