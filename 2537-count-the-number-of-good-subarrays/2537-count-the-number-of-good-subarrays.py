class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        count = 0
        left = 0
        current = Counter()
        c = 0
        for right, v in enumerate(nums):
            
            if current[v] > 0:
                c += current[v]
            
            current[v] += 1
            
            while c >= k:
                count += len(nums) - right
                current[nums[left]] -= 1
                c -= current[nums[left]]
                left += 1
        
        return count