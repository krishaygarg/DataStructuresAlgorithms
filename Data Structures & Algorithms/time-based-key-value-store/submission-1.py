from collections import defaultdict
import bisect
class TimeMap:

    def __init__(self):
        self.timestamps = defaultdict(list)
        self.values = defaultdict(list)
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timestamps[key].append(timestamp)
        self.values[key].append(value)
    def get(self, key: str, timestamp: int) -> str:
        timestampList = self.timestamps[key]
        index = bisect.bisect_right(timestampList,timestamp)-1
        # print(index)
        if index == -1:
            return ""
        return self.values[key][index]
