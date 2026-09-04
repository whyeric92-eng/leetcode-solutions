#include <string>
#include <vector>
using namespace std;
class Solution {
public:
    bool judge(vector<string>& strs, int i) {
        char temp = strs[0][i];
        for (int j = 1; j < strs.size(); j++) {
            if (i >= strs[j].size() || temp != strs[j][i]) {
                return false;
            }
        }
        return true;
    }
    string longestCommonPrefix(vector<string>& strs) {
        string res = "";
        for (int i = 0; i < strs[0].size(); i++) {
            if (judge(strs, i)) {
                res = res + strs[0][i];
            } else {
                return res;
            }
        }
        return res;
    }
};