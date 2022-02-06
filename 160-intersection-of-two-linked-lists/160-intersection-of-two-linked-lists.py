# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        tmp = headA
        
        keep = set()
        
        while tmp:
            keep.add(tmp)
            tmp = tmp.next
        
        tmp = headB
        
        while tmp:
            if tmp in keep:
                return tmp
            
            tmp = tmp.next
            
        return None
        