class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        

        j = 0
        
        i = 0
        n1 = len(nums1)
        n2 = len(nums2)
        while i < n1 and j < n2:
            if nums1[i] == nums2[j]:
                return nums1[i]
            if nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return -1
        