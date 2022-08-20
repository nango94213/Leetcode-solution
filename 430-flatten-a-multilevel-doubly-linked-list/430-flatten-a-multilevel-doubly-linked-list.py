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
        fake = Node(None, None, head, None)
        
        pre = fake
        
        while stack:
            current = stack.pop()
            
            pre.next = current
            current.prev = pre
            
            if current.next:
                stack.append(current.next)
            
            if current.child:
                stack.append(current.child)
                current.child = None
            
            pre = current
        
        fake.next.prev = None
        
        return fake.next
            