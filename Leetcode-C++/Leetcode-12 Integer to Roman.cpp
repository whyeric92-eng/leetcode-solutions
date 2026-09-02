#include <vector>
#include <unordered_map>
#include <string>
using namespace std;

class Solution {
public:
    string repeat(const string& s, int n) {
            string result;
            for (int i = 0; i < n; i++) {
                result += s;
            }
            return result;
        }

    string intToRoman(int num) {
        unordered_map<int, string> dict = {
            {1, "I"}, {5, "V"}, {10, "X"}, {50, "L"}, {100, "C"}, {500, "D"}, {1000, "M"}
        };
        string res = "";
        int temp, base = 1;
        while (num > 0) {
            temp = num % 10;
            if (temp != 4 && temp != 9) {
                if (temp < 5) {
                    res = repeat(dict[base], temp) + res;
                } else {
                    res = dict[base * 5] + repeat(dict[base], temp - 5) + res;
                }
            } else if (temp == 4) {
                res = dict[base] + dict[base * 5] + res;
            } else {
                res = dict[base] + dict[base * 10] + res;
            }
            num /= 10;
            base *= 10;
        }
        return res;
    }
};