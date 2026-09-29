#include <string>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    bool isValid(string s) {
        // vector 当栈用: 没有 push/pop, 要用 push_back()/pop_back()
        vector<char> res = {};
        unordered_map<char,char> dict = {
            {'(', ')'}, {'{', '}'}, {'[', ']'}
        };
        int n = int(s.size());
        for (int i = 0; i < n; i++) {
            if (dict.contains(s[i])) {
                res.push_back(s[i]);
            // 不支持负索引 res[-1] (越界是未定义行为), 栈顶用 res.back()
            // 必须先判空: 空栈调用 back() 会崩
            // dict[key] 在 key 不存在时会插入新元素, 只读时更稳妥用 dict.at()
            } else if (!res.empty() && dict[res.back()] == s[i]) {
                res.pop_back();
            } else {
                return false;
            }
        }
        // 不能写 res == {}, 判空用 res.empty()
        return res.empty();
    }
};
