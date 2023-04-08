class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        count = Counter(nums)
        
        major = max(count.values())
        
        for c in count:
            if count[c] == major:
                return c