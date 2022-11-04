class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        
        def kth(a, b, k):
            if not a:
                return b[k]
            if not b:
                return a[k]
            
            ai = len(a) // 2
            bi = len(b) // 2
            ma = a[ai]
            mb = b[bi]
            
            if ai + bi < k:
                if ma > mb:
                    return kth(a, b[bi+1:], k - bi - 1)
                else:
                    return kth(a[ai+1:], b, k - ai - 1)
            else:
                if ma > mb:
                    return kth(a[:ai], b, k)
                else:
                    return kth(a, b[:bi], k)
                
        l = len(nums1) + len(nums2)
        if l % 2 == 0:
            return (kth(nums1, nums2, l//2) + kth(nums1, nums2, l//2-1)) / 2
        else:
            return kth(nums1, nums2, l//2)
        