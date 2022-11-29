
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        
        keys = list(count.keys())
        
        def partition(left, right, pivot):
            keys[pivot], keys[right] = keys[right], keys[pivot]
            
            i = left
            for j in range(left, right):
                if count[keys[j]] < count[keys[right]]:
                    keys[i], keys[j] = keys[j], keys[i]
                    i += 1
            keys[i], keys[right] = keys[right], keys[i]
            return i
        
        def search(left, right):
            if left == right:
                return keys[left:]
            
            pivot = random.randint(left, right)
            i = partition(left, right, pivot)
            
            if i == len(keys) - k:
                return keys[i:]
            if i > len(keys) - k:
                return search(left, i-1)
            else:
                return search(i+1, right)
        
        return search(0, len(keys)-1)