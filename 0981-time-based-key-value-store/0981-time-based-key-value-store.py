import collections
class TimeMap(object):

    def __init__(self):
        self.time = collections.defaultdict(list)
        

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.time[key].append((value, timestamp))
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        check = self.time[key]
        left = 0
        right = len(check) - 1
        
        while left <= right:
            mid = (left+right) // 2
            if check[mid][1] == timestamp:
                return check[mid][0]
            if check[mid][1] > timestamp:
                right = mid - 1
            else:
                left = mid + 1
        return check[right][0] if right != -1 else ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)