#解法一
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        def is_subsit(lst1,lst2):
            for char in lst1:
                if char not in lst2:
                    return False
            return True
        s_list=[char for char in s]
        res=[s_list[0]]
        n=len(s_list)
        for i in range(1,n):
            if s_list[i] not in res:
                con=False
                for j in range(len(res)):
                    if is_subsit(res[j:],s_list[i:]) and res[j]>s_list[i]:
                        res_new=res[:j]
                        res_new.append(s_list[i])
                        con=True
                        break
                if con:
                    res=res_new
                if not con:
                    res.append(s_list[i])
        res_str="".join(res)
        return res_str
#这个解法的思路就是正常手算的思路，就是这个最不好(导致时间复杂度骤增)的一步就是is_subsit(res[j:],s_list[i:])
#因为正着看的话，后面的所有都必须要考虑，这样才确认是否被替换

#解法二
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        last_index={c:i for i,c in enumerate(s)}
        stack=[]
        seen=[]
        for i,c in enumerate(s):
            if c in seen:
                continue
            while stack and stack[-1]>c and last_index[stack[-1]]>i:
                char=stack.pop()
                seen.remove(char)
            stack.append(c)
            seen.append(c)
        return "".join(stack)
#这个方法很绝妙：1.last_index的处理(处理成字典，而且这样子就是最后一次出现的位置了),注意i,c这个写前面的默认为index了
#2.和上一个方法不同的就是，这个倒着来判断，然后用一个while就搞定了，这样就节约了很多时间复杂度