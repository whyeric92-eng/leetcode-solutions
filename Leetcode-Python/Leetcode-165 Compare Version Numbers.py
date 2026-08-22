class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1=version1.split(".")
        ver2=version2.split(".")
        # 这个时候是切成str然后放进list里面 所以后面需要统一换成int
        idx=0
        n=max(len(ver1),len(ver2))
        ver1=ver1+[0]*(n-len(ver1))
        ver2=ver2+[0]*(n-len(ver2))
        while idx<n:
            if int(ver1[idx])>int(ver2[idx]):
                return 1
            elif int(ver1[idx])<int(ver2[idx]):
                return -1
            idx+=1
        return 0

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        i, j = 0, 0
        m, n = len(version1), len(version2)

        while i < m or j < n:
            num1, num2 = 0, 0

            # 提取 version1 当前段的数字
            while i < m and version1[i] != '.':
                num1 = num1 * 10 + int(version1[i])
                i += 1

            # 提取 version2 当前段的数字
            while j < n and version2[j] != '.':
                num2 = num2 * 10 + int(version2[j])
                j += 1

            if num1 > num2: return 1
            if num1 < num2: return -1

            i += 1  # 跳过 '.'
            j += 1
        
        return 0
# two pointers解法 优化空间复杂度为 O(1)