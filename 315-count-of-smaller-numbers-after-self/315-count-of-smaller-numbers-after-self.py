class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
    
        arr = [(v, i) for i, v in enumerate(nums)]
        res = [0] * len(nums)
        def mergeSort(arr):
             if len(arr) > 1:
            
                 mid = len(arr)//2
  
        # Dividing the array elements
                 L = arr[:mid]
  
        # into 2 halves
                 R = arr[mid:]
  
        # Sorting the first half
                 mergeSort(L)
  
        # Sorting the second half
                 mergeSort(R)
  
                 i = j = k = 0
  
        # Copy data to temp arrays L[] and R[]
                 while i < len(L) and j < len(R):
                    if L[i][0] <= R[j][0]:
                           arr[k] = L[i]
            
                           res[L[i][1]] += j
                           i += 1
                
                    else:

                            arr[k] = R[j]
                            j += 1
                    k += 1
  
        # Checking if any element was left
                 while i < len(L):
                        arr[k] = L[i]
                        res[L[i][1]] += j
                        i += 1
                        k += 1
  
                 while j < len(R):
                        arr[k] = R[j]
                        j += 1
                        k += 1
        mergeSort(arr)
        return res
