class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def partition(left, right, pivot_index):
            
            pivot = nums[pivot_index]
            
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
            i = left
            
            for j in range(left, right):
                if nums[j] < pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            
            nums[right], nums[i] = nums[i], nums[right]
            
            return i
        
        def select(left, right):
            
            if left == right:
                return nums[left]
            
            pivot_index = random.randint(left, right)
            
            i = partition(left, right, pivot_index)
            
            if i == len(nums) - k:
                return nums[i]
            
            if i > len(nums) - k:
                return select(left, i-1)
            else:
                return select(i+1, right)
        
        return select(0, len(nums)-1)
            
            