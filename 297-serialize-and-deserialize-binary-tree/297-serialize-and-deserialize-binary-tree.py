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
        
        def to_string(node):
            if node:
                res.append(str(node.val)+',')
                to_string(node.left)
                to_string(node.right)
            else:
                res.append('None,')
        
        to_string(root)
        
        return ''.join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        def to_tree():
            if l[0] == 'None':
                l.popleft()
                return
            
            root = TreeNode(l[0])
            l.popleft()
            
            root.left = to_tree()
            root.right = to_tree()
            
            return root
        
        l = data.split(',')
        l = collections.deque(l)
        return to_tree()
                
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))