# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = []
        
        for i, link in enumerate(lists):
            if link:
                heapq.heappush(h, (link.val, i))
        
        head = current = ListNode(0)
        
        while h:
            value, index = heapq.heappop(h)
            
            current.next = ListNode(value)
            
            current = current.next
            
            lists[index] = lists[index].next
            
            if lists[index]:
                heapq.heappush(h, (lists[index].val, index))
        
        return head.next
            