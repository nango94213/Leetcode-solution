"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        stack = [head]
        fake = Node(None, None, None, None)
        
        pre = fake
        
        while stack:
            current = stack.pop()
            
            pre.next = current
            current.prev = pre
            
            pre = pre.next
            
            if current.next:
                stack.append(current.next)
            
            if current.child:
                stack.append(current.child)
                current.child = None
            
            
        
        head.prev = None
        
        return head
            