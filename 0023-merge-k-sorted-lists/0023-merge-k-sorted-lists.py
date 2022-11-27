# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        h = []
        
        for i, v in enumerate(lists):
            if v:
                heapq.heappush(h, (v.val, i))
        
        head = ListNode(0)
        p = head
        
        while h:
            current, index = heapq.heappop(h)
            
            p.next = ListNode(current)
            p = p.next
            
            lists[index] = lists[index].next
            
            if lists[index]:
                heapq.heappush(h, (lists[index].val, index))
        
        return head.next