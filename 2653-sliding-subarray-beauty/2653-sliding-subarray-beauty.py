import heapq
class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        left = 0
        dic = Counter()
        res = []
        heap = []
        seen = set()
        for right in range(len(nums)):
            if nums[right] < 0:
                dic[nums[right]] += 1
            
            
            if right - left + 1 > k:
                dic[nums[left]] -= 1
                left += 1
            
            count = 0

            if right >= k - 1:

                for j in range(-50, 0):
                    if j in dic:
                        count += dic[j]
                    if count >= x:
                        res.append(j)
                        break
                else:
                    res.append(0)
        return res
                
                    
            