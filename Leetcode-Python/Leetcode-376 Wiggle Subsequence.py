class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        diff=[]
        for i in range(n-1):
            diff.append(nums[i+1]-nums[i])
        res=1
        for i in range(len(diff)):
            if diff[i]==0:
                continue
            else:
                if res==1:
                    res+=1
                    val=diff[i]
                elif val*diff[i]<0:
                    val=diff[i]
                    res+=1
        return res
#核心：如果是同号，应该算到前面(正的更正，负的更负)，不应该算到后面！！！！