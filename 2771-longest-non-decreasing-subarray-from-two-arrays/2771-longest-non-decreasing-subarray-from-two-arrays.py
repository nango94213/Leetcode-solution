class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[1, 1] for _ in range(len(nums1))]
        res = 1
        for i in range(1, len(nums1)):
            if nums1[i] >= nums1[i-1]:
                dp[i][0] = max(dp[i][0], dp[i-1][0] + 1)
            if nums1[i] >= nums2[i-1]:
                dp[i][0] = max(dp[i][0], dp[i-1][1] + 1)
            if nums2[i] >= nums2[i-1]:
                dp[i][1] = max(dp[i][1], dp[i-1][1] + 1)
            if nums2[i] >= nums1[i-1]:
                dp[i][1] = max(dp[i][1], dp[i-1][0] + 1)
            res = max(res, dp[i][0], dp[i][1])
        return res
        