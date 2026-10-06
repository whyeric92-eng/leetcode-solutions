import heapq
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        def convert(nums):
            return nums[0]**2 + nums[1]**2
        new_nums = [(-convert(nums),nums) for nums in points]
        h = []
        for point in new_nums:
            if len(h) < k:
                heapq.heappush(h, point)
            elif h[0][0] < point[0]:
                heapq.heappop(h)
                heapq.heappush(h, point)
        return [res[1] for res in h]