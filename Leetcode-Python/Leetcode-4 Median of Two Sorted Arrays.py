#解法一
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        nums1.sort()
        n=len(nums1)
        return (nums1[(n-1)//2]+nums1[n//2])/2.0
#这个解法最简单，同时时间复杂度也最高，唯一需要注意的点就是最后/2.0得到float

#解法二
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m=len(nums1)
        n=len(nums2)
        i,j=0,0
        prev,cur=0,0
        k=(m+n)//2
        for _ in range(k+1):
            prev=cur
            if i<m and (j>=n or nums1[i]<nums2[j]):
                cur=nums1[i]
                i+=1
            else:
                cur=nums2[j]
                j+=1
        return (prev+cur)/2.0 if (m+n)%2==0 else cur
#这个解法时间复杂度稍微降低了一点，主要是运用双指针来判断中位数的大致位置
#这个解法运营prev和cur来存储最后两次比较的结果(这两个结果也是算中位数时可能用到的)
#if i<m and (j>=n or nums1[i]<nums2[j]):这个判定条件是很巧妙的，首先要i<m并且要么j把n走完了要么nums1[i]<nums2[j]，i才会推进到下一个

#解法三
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1)>len(nums2):
            nums1,nums2=nums2,nums1
        m=len(nums1)
        n=len(nums2)
        half=(m+n)//2
        left,right=0,m
        while left<=right:
            i=(left+right)//2
            j=half-i
            nums1_left=nums1[i-1] if i>0 else float('-inf')
            nums1_right=nums1[i] if i<m else float('inf')
            nums2_left = nums2[j-1] if j > 0 else float('-inf')
            nums2_right = nums2[j] if j < n else float('inf')
            if nums1_left<=nums2_right and nums1_right>=nums2_left:
                if (m+n)%2==0:
                    return (max(nums1_left,nums2_left)+min(nums1_right,nums2_right))/2.0  
                else:
                    return min(nums1_right,nums2_right)
            elif nums1_left>nums2_right:
                right=i-1
            else:
                left=i+1
#这个解法是最复杂的，但也是时间复杂度最低的
#运用binary search(甚至不需要把两个nums合起来，用一个指针，大致分成左边和右边来判断)
#这道题的难点就在于如何找到这个指针(运用binary search)，从m//2处开始找，来判断是否满足条件
#注意的点：1.保证nums1的长度小于nums2的长度，这样可以确保不会越界 
#2.nums1_left=nums1[i-1] if i>0 else float('-inf')这种处理很巧妙，处理成正/负无穷，不会影响大小比较(当左边/右边没有元素的时候)