# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        
        fast = head.next
        slow = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        start = slow.next
        slow.next = None
        
        left, right = self.sortList(head), self.sortList(start)
        
        return self.merge(left, right)
    
    def merge(self, left, right):
        
        if not left or not right:
            return left or right
        
        fake = ListNode(0)
        p = fake
        
        while left and right:
            if left.val < right.val:
                p.next = left
                p = p.next
                left = left.next
            else:
                p.next = right
                p = p.next
                right = right.next
        p.next = left or right
        return fake.next