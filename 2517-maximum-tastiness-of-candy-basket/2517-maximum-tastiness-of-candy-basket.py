class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        
        left = 0
        right = price[-1] - price[0]
        ans = -1
        
        while left <= right:
            mid = (left+right)//2
            
            count =  1
            prev = price[0]
            for i in range(1, len(price)):
                if price[i] - prev >= mid:
                    count += 1
                    prev = price[i]
            
            if count >= k:
                left = mid + 1
                ans = mid
            else:
                right = mid - 1
                
        return ans