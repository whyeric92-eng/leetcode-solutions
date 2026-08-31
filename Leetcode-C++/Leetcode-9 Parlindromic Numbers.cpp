#include <string>
using namespace std;

class Solution {
public:
    bool isPalindrome(int x) {
       string xx = to_string(x);
       string temp = "";
       for (int i = 0; i < xx.size(); i++) {
            temp = xx[i] + temp;
       } 
       if (temp == xx) {
        return true;
       } else {
        return false;
       }
    }
};

bool isPalindrome(int x) {
    if (x < 0 || (x % 10 == 0 && x != 0)) return false;
    
    int reverted = 0;
    while (x > reverted) {
        reverted = reverted * 10 + x % 10;
        x /= 10;
    }
    
    return x == reverted || x == reverted / 10;
}
// 纯数学解法 额外空间O(1)

bool isPalindrome(int x) {
    string xx = to_string(x);
    string temp = xx;
    reverse(temp.begin(), temp.end());
    return temp == xx;
}
// C++的reverse写法 