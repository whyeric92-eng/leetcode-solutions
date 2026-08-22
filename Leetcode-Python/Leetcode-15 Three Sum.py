#解法一
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n=len(nums)
        nums.sort()
        output=[]
        for i in range(n-2):
            ans=-nums[i]
            if ans<nums[i+1]:
                return output
            else:
                hashmap={}
                for j in range(i+1,n):
                    ans1=ans-nums[j]
                    if ans1 in hashmap:
                        list1=[nums[i],ans1,nums[j]]
                        list1.sort()
                        if list1 in output:
                            pass
                        else:
                            output.append(list1)
                    else:
                        hashmap[nums[j]] = True 
        return output
#这个hashmap的优点在于查找的时候时间复杂度是O(1)而非O(n)
#注意点：hashmap相当于字典，用{}，这个nums[j]相当于是key，if ans1 in hashmap，这个判断也是在看ans1在不在haspmap的key里面

#解法二
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n=len(nums)
        nums.sort()
        output=[]
        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left=i+1
            right=n-1
            while left<right:
                if nums[left]+nums[right]==-nums[i]:
                    output.append([nums[i],nums[left],nums[right]])
                    while left<right and nums[left]==nums[left+1]:
                        left +=1
                    while right>left and nums[right]==nums[right-1]:
                        right -=1
                    left+=1
                    right-=1
                elif nums[left]+nums[right]>-nums[i]:
                    right-=1
                elif nums[left]+nums[right]<-nums[i]:
                    left+=1
        return output
#给定i，然后后面来“夹”正确的解
#细节注意：1.必须要加i>0，因为i=0的时候，i-1=-1（默认为了最后一个）
#避免重复的方法:最开始的那个nums[i]==nums[i-1]的话，直接过，写continue是最优解，不要写i+=1(会引发错乱)
#后面的话：left和right一样的逻辑，一样就跳过，但要注意最初限制(left<right)