# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = ListNode(0)
        fake = head
        carry = 0
        
        while l1 or l2:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            
            total = n1 + n2 + carry
            
            carry = total // 10
            
            fake.next = ListNode(total%10)
            
            if l1:
                l1 = l1.next
                
            if l2:
                l2 = l2.next
            
            fake = fake.next
        
        if carry == 1:
            fake.next = ListNode(1)
        
        return head.next
            
        