# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        
        seen = set()
        delete = set()
        
        pointer = head
        
        while pointer:
            if pointer.val in seen:
                delete.add(pointer.val)
            else:
                seen.add(pointer.val)
            
            pointer = pointer.next
                
            

        tmp = ListNode(0)
        tmp.next = head
        pointer = tmp
        
        while pointer.next:
            if pointer.next.val in delete:
                pointer.next = pointer.next.next
            else:
                pointer = pointer.next
        
        return tmp.next
        