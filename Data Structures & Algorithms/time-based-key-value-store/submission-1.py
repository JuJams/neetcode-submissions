class TimeMap:

    def __init__(self):
        # key: list of [val, stamptime]
        self.store = {} # key is string and the value is list of lists

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        result = ""
        values = self.store.get(key, [])
        # binary search
        left = 0
        right = len(values) - 1
        while left <= right:
            mid = (left + right) // 2
            if values[mid][1] == timestamp:
                return values[mid][0]
            elif values[mid][1] <= timestamp:
                result = values[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        return result


