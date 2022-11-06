class TimeMap(object):

    def __init__(self):
        self.dic = collections.defaultdict(list)

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.dic[key].append((timestamp, value))
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        left = 0
        right = len(self.dic[key]) - 1
        values = self.dic[key]
        while left <= right:
            mid = (left+right) // 2
            if values[mid][0] == timestamp:
                right = mid
                break
            if values[mid][0] > timestamp:
                right = mid - 1
            if values[mid][0] < timestamp:
                left = mid + 1
                
        return "" if right == -1 else values[right][1]
            
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)