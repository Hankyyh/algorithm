class TimeMap:

    def __init__(self):
        self.dic = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append([timestamp, value])

    def get(self, key, timestamp):
        if not self.dic[key]:
            return ""
        arr = self.dic[key]
        n = len(arr)

        left = 0
        right = n - 1

        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid][0] < timestamp:
                left = mid + 1
            elif arr[mid][0] > timestamp:
                right = mid - 1
            elif arr[mid][0] == timestamp:
                return arr[mid][1]
        if arr[right][0] > timestamp:
            return ""
        return arr[right][1]



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)