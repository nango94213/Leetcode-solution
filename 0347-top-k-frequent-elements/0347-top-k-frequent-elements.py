import random
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        
        nums = list(count.keys())

        def partition(left, right, pivot):
            print(pivot)
            nums[pivot], nums[right] = nums[right], nums[pivot]
            
            i = left
            for j in range(left, right):
                if count[nums[j]] < count[nums[right]]:
                    nums[j], nums[i] = nums[i], nums[j]
                    i += 1
            
            nums[i], nums[right] = nums[right], nums[i]
            
            return i
        
        def search(left, right):
            if left == right:
                return nums[left:]
            
            p = random.randint(left, right)
            i = partition(left, right, p)
            
            if i == len(nums) - k:
                return nums[i:]
            if i < len(nums) - k:
                return search(i+1, right)
            if i > len(nums) - k:
                return search(left, i-1)
        
        return search(0, len(nums)-1)