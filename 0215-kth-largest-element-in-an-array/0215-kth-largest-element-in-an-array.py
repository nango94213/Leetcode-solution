class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def partition(left, right, pivot):
            nums[pivot], nums[right] = nums[pivot], nums[right]
            
            i = left
            for j in range(left, right):
                if nums[j] < nums[right]:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[right] = nums[right], nums[i]
            return i
        
        def search(left, right):
            if left == right:
                return nums[left]
            
            pivot = random.randint(left, right)
            i = partition(left, right, pivot)
            
            if i == len(nums) - k:
                return nums[i]
            
            if i > len(nums) - k:
                return search(left, i-1)
            else:
                return search(i+1, right)
        
        return search(0, len(nums)-1)
        