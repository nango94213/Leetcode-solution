# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def reverse(node, t):
            
            prev = None
            
            while t > 0:
                t -= 1
                
                hold = node.next
                node.next = prev
                prev = node
                node = hold
            
            return prev
        
        
        ptr = head
        new = None
        tail = None
        
        while ptr:
            
            count = 0
            
            while count < k and ptr:
                count += 1
                ptr = ptr.next
            
            if count == k:
                rev = reverse(head, k)
                
                if not new:
                    new = rev
                
                if tail:
                    tail.next = rev
                    
                tail = head
                head = ptr
            
        if tail:
            tail.next = head
        
        return new if new else head