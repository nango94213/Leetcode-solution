# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        point = head
        
        res = []
        
        while point:
            
            res.append(point.val)
            point = point.next
        
        
        one = k - 1
        two = len(res) - k
        
        res[one], res[two] = res[two], res[one]
        
        
        final = ListNode(0)
        
        tmp = final
        
        
        for i in res:
            
            tmp.next = ListNode(i)
            tmp = tmp.next
        
        
        return final.next