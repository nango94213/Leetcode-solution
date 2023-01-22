class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if k == 0:
            if nums1 == nums2:
                return 0
            else:
                return -1
        diff = [nums1[i]-nums2[i] for i in range(len(nums1))]
        
        if sum(diff) != 0:
            return -1
        
        res = 0
        for n in diff:
            if n % k != 0:
                return -1
            if n > 0:
                res += n // k
        
        return res