class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap={}
        for i,num in enumerate(nums):
            complement=target-num
            if complement in hashmap:
                return [hashmap[complement] ,i]
            else:
                hashmap[num]=i
#注意点：哈希表的使用，在里面？输出，不在里面？存入
#注意这个哈希表它的元素是i，然后它的index才是num，因为我们要求输出的是原数列的i（index）
#enumerate的用法，同时告诉我元素和index，适用于任何iterable的东西
#哈希表的优势体现在查找的时候，复杂程度为O(1)，不像普通的查找需要一个一个去看