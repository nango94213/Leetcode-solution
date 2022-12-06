class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        total = n * (n-1) * (n-2) // 6
        
        count = Counter(nums)
        
        for v in count.values():
            if v < 2:
                continue
            
            three = v * (v-1) * (v-2) // 6
            two = (n-v) * v * (v-1) // 2
            total -= three + two
        return total