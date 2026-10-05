from typing import List
import heapq
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hash_map = {}
        h = []
        res = []
        heapq.heapify(h)
        for num in nums:
            if num in hash_map:
                hash_map[num] += 1
            else:
                hash_map[num] = 1
        for num, freq in hash_map.items():
            if len(h) < k:
                heapq.heappush(h, (freq, num))
            elif h[0][0] < freq:
                heapq.heappop(h)
                heapq.heappush(h, (freq, num))
        for pair in h:
            res.append(pair[1])
        return res


#精简版
import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        h = []
        for num, freq in Counter(nums).items():
            if len(h) < k:
                heapq.heappush(h, (freq, num))
            elif h[0][0] < freq:
                heapq.heapreplace(h, (freq, num))
        return [num for _, num in h]