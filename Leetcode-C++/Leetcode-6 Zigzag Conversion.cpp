#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows == 1) {
            return s;
        }
        vector <string> rows(numRows, "");
        int n = int(s.size());
        int divider = 2*numRows-2;
        int temp;
        auto convert = [](int index, int divider) {
            int remainer;
            remainer = index % divider;
            if (remainer > (divider/2)) {
                return divider - remainer;
            } else {
                return remainer;
            }
        };
        for (int i = 0; i < n; i++) {
            temp = convert(i,divider);
            rows[temp]+=s[i];
        }
        string result;
        for (const string& row : rows) {
            result += row;
        }
        return result;
    }
};

class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows == 1) return s;

        vector<string> rows(numRows, "");
        int divider = 2 * numRows - 2;

        auto getRow = [](int index, int divider) {
            int remainder = index % divider;
            return remainder > divider / 2 ? divider - remainder : remainder;
        };

        for (int i = 0; i < (int)s.size(); i++) {
            rows[getRow(i, divider)] += s[i];
        }

        string result;
        for (const string& row : rows) {
            result += row;
        }
        return result;
    }
};
// 更加简洁优雅的写法