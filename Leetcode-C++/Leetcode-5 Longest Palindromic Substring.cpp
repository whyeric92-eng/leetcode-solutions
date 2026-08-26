#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    string longestPalindrome(string s) {
        int n = int(s.size());
        string res = "";
        vector<vector<bool>> dp(n,vector<bool>(n,false));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i+1; j++) {
                if (s[i]==s[j] && (i-j<=2 || dp[j+1][i-1])) {
            // 关键要点是要先规定上界往回遍历 因为往回遍历的dp才是已知的
            // 不需要单独跑一次dp[i][i]=true 现在的写法可以覆盖 而且更简洁
                    dp[j][i]=true;
                    if (i-j+1 > int(res.size())) {
                    res = s.substr(j,i-j+1);
                    }
                }
            }
        }
        return res;
    }
};

class Solution {
public:
    string longestPalindrome(string s) {
        // 预处理：字符间插入'#'，首尾加哨兵'^'和'$'
        // 这样奇偶长度的回文串都能统一按“以某点为中心”处理，哨兵还能防止扩展时越界
        string temp = "^#";
        for (char c: s) {
            temp+=c;
            temp+="#";
        }
        temp+="$";
        int n = int(temp.size());
        // p[i] 表示以 temp[i] 为中心能扩展出的回文半径（不含中心本身）
        vector <int> p(n,0*n);
        // center/right：当前遍历过程中回文串能达到的最右边界，以及对应的中心位置
        int center = 0, right = 0;
        int mirror, center_index, start;
        int max_len = 0;
        for (int i = 1; i < n-1; i++) {
            if (i < right) {
                // i 落在已知回文的右边界内，可以利用对称性：
                // i 关于 center 的镜像点 mirror 的回文半径可以作为 p[i] 的初始值（回文性质保证对称）
                mirror = 2*center - i;
                // 但镜像回文可能超出当前右边界right，超出部分尚未验证，因此要取min做截断
                p[i] = min(right-i, p[mirror]);
            }
            // 中心扩展：从当前已知的p[i]继续往两边试探
            // 哨兵'^'和'$'保证左右扩展不会数组越界
            while (temp[i+p[i]+1] == temp[i-p[i]-1]) {
                p[i] += 1;
            }
            // 如果当前中心扩展出的回文串超过了之前记录的right，更新center和right
            if (i+p[i] > right) {
                right = i+p[i];
                center=i;
            }
        }
        // 遍历所有中心，找到回文半径最大的位置，即为最长回文串
        for (int i = 0; i < n; i++) {
            if (p[i] > max_len) {
                max_len = p[i];
                center_index = i;
            }
        }
        // 将预处理字符串中的中心位置换算回原字符串的起始下标
        // (center_index - max_len) 是回文串在temp中的起始位置（含'#'），除以2正好抵消插入的'#'，得到原串下标
        start = (center_index - max_len)/2;
        return s.substr(start, max_len);
    }
};