# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        current = head
        
        while current and current.next:
            
            temp = ListNode(gcd(current.val, current.next.val))
            temp.next = current.next
            current.next = temp
            current = temp.next
        
        return head
            
            
        