class Solution:
    def heapify(self, A, i, heap_size):
        l = 2*i + 1
        r = 2*i + 2
        if l >= heap_size:
            return
        if r < heap_size and A[r] > A[l]:
            largest = r
        else:
            largest = l
        if A[i] < A[largest]:
            A[i], A[largest] = A[largest], A[i]
            self.heapify(A, largest, heap_size)

    def build_heap(self, A):
        heap_size = len(A)
        for i in range(heap_size//2-1, -1, -1):
            self.heapify(A, i, heap_size)
        return A

    def sortArray(self, nums: list[int]) -> list[int]:
        heap_size = len(nums)
        nums = self.build_heap(nums)
        for i in range(heap_size-1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            heap_size -= 1
            self.heapify(nums, 0, heap_size)
        return nums

#这个还真是max_heap最合适 得到max_heap之后不断取出h[0]放到最底部(此时h[0]为当前最大)