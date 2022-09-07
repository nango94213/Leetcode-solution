"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        dic = {}
        
        p = head
        
        while p:
            dic[p] = Node(p.val)
            p = p.next
        
        
        p = head
        
        while p:
            
            dic[p].next = dic.get(p.next)
            dic[p].random = dic.get(p.random)
            
            p = p.next
        
        return dic.get(head)
            
        