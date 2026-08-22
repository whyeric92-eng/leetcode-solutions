#解法一
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = list(map(str, nums))
        nums.sort(key=lambda x: x*10, reverse=True)
        res = ''.join(nums)
        if res[0] == '0':
            res = '0'
        return res
#这道题拼接出最大数字，最简单的就是先按首个数字来排序，这样是最简单的情况
#这道题难就难在首字母相同的时候该怎么排序，推荐的解法就是对这个字符串重复很多次再来进行比较大小，eg. 3和30谁在前面也可以比较了
#经验性技巧：一般重复10次就绰绰有余了
#新技巧：nums.sort(key=lambda x:分类标准(目前默认为升序),reverse=True/False(来决定是否翻转))

#解法二
from functools import cmp_to_key
#引入cmp_to_key这个函数(这是个固定的名字)
def compare(a, b):
    if a + b > b + a:
        return -1
    elif a + b < b + a:
        return 1
    else:
        return 0
#定义compare函数(用于比较谁在前面)
nums = [3, 30, 34, 5, 9]
nums_str = list(map(str, nums))
sorted_nums = sorted(nums_str, key=cmp_to_key(compare))
#key=cmp_to_key(compare)比较的关键就是定义的这个compare函数
res = ''.join(sorted_nums)
print(res)  # 9534330
