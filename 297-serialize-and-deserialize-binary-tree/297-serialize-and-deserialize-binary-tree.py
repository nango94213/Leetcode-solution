# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        res = []
        
        def dfs(node):
            
            if node:
                res.append(str(node.val))
                
                dfs(node.left)
                dfs(node.right)
            else:
                res.append('None')
        
        dfs(root)
        
        return ','.join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def dfs():
            if l:
                val = l.popleft()
                
                if val == 'None':
                    return 
                
                root = TreeNode(val)
                
                root.left = dfs()
                root.right = dfs()
                
                return root

        
        
        
        l = data.split(',')
        l = collections.deque(l)
        
        return dfs()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))