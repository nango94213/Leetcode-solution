# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        values = []
        
        p = head
        
        n = 0
        while p:
            values.append(p.val)
            p = p.next
            n += 1
        
        res = 0
        
        for i in range(n//2-1, n):
            res = max(res, values[i]+values[n-1-i])
        
        return res
            
        