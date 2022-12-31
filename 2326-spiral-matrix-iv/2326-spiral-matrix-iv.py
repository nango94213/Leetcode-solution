# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1] * n for _ in range(m)]
        
        left = 0
        right = n - 1
        top = 0
        bottom = m - 1
        
        while head:
 
            for i in range(left, right+1):
                if not head:
                    break
                matrix[top][i] = head.val
                head = head.next
            
            for i in range(top+1, bottom+1):
                if not head:
                    break
                matrix[i][right] = head.val
                head = head.next
            
            if top != bottom:
                for i in range(right-1, left-1, -1):
                    if not head:
                        break
                    matrix[bottom][i] = head.val
                    head = head.next
            
            if left != right:
                for i in range(bottom-1, top, -1):
                    if not head:
                        break
                    matrix[i][left] = head.val
                    head = head.next
    
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        
        return matrix