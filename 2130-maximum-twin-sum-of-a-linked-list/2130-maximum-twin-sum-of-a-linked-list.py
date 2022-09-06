# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        '''values = []
        
        p = head
        
        n = 0
        while p:
            values.append(p.val)
            p = p.next
            n += 1
        
        res = 0
        
        for i in range(n//2-1, n):
            res = max(res, values[i]+values[n-1-i])
        
        return res'''
        
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        pre, current = None, slow
        
        while current:
            current.next, pre, current = pre, current, current.next
        
        res = 0
        
     
        while pre:
            res = max(res, head.val+pre.val)
            
            head = head.next
            pre = pre.next
        
        return res
            
            
        