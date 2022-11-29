# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def reverse(sub, k):
            
            prev = None
            i = 0
            while i < k:
                hold = sub.next
                sub.next = prev
                prev = sub
                sub = hold
                
                i += 1
            return prev
        
        ptr = head
        tail = None
        new = None
        
        while ptr:
            
            i = 0
            while i < k and ptr:
                ptr = ptr.next
                i += 1
            
            if i == k:
                rev = reverse(head, k)
                if not tail:
                    new = rev
                
                if tail:
                    tail.next = rev
                
                tail = head
                head = ptr
        tail.next = head
        return new
            
            
            