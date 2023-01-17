class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        count = 0
        left = 0
        current = Counter()
        c = 0
        n = len(nums)
        for right, v in enumerate(nums):
            
            c += current[v]
            
            current[v] += 1
            
            while c >= k:
                count += n - right
                current[nums[left]] -= 1
                c -= current[nums[left]]
                left += 1
        
        return count