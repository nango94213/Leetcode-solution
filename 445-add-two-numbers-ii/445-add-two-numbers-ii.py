# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        stack1 = []
        stack2 = []
        
        while l1 or l2:
            if l1:
                stack1.append(l1.val)
                l1  =  l1.next
            
            if l2:
                stack2.append(l2.val)
                l2 = l2.next
        
        head = None
        carry  =  0
        
        while stack1 or stack2:
            n1 = stack1.pop() if stack1 else 0
            n2 = stack2.pop() if stack2 else 0
            
            summ = n1 + n2 + carry
            carry = summ // 10
            
            node = ListNode(summ%10)
            
            node.next = head
            head = node
        
        if carry == 1:
            node = ListNode(1)
            
            node.next = head
            head = node
        
        return head
            