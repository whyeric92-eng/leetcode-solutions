#include <string>
#include <unordered_map>
#include <algorithm>
using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int res = 0;
        int start = 0;
        unordered_map<char,int> dict;
        for (int i = 0; i < int(s.size()); i++ ) {
            // s.size()返回的不是int 需要转化
            if (dict.count(s[i])) {
                start = max(start, dict[s[i]]+1);
                // 一定要注意是 max(start,...) 因为要判断重复的这个char在不在当前的[start,i]的这个窗口内
            }
            dict[s[i]] = i;
            res = max(res, i-start+1);
            // 建议每次更新res
            // 维护[start,i]是无重复的substring(作为sliding window)
        }
        return res;
    }
};