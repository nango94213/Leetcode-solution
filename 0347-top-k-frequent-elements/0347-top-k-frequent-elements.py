import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        
        keys = list(count.keys())
        
        def partition(left, right, pivot_index):
        
           pivot = keys[pivot_index]
        
           keys[pivot_index], keys[right] = keys[right], keys[pivot_index]
        
           i = left
        
           for j in range(left, right):
                if count[keys[j]] < count[pivot]:
                    keys[i], keys[j] = keys[j], keys[i]
                    i += 1
        
           keys[i], keys[right] = keys[right], keys[i]
        
           return i
    
        def search(left, right):
        
            if left == right:
                return keys[right:]
           
            pivot_index = random.randint(left, right)
            i = partition(left, right, pivot_index)
            
            if i == len(keys) - k:
                return keys[i:]
            
            if i < len(keys) - k:
                return search(i+1, right)
            else:
                return search(left, i-1)
        
        return search(0, len(keys)-1)
        
        
        