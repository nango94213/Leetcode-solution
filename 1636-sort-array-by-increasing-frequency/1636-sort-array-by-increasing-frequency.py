class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        
        count = Counter(nums)
        
        nums = sorted(nums, key=lambda x: (count.get(x), -x))
        
        return nums
        