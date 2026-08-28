#include <climits>
#include <string>
using namespace std;

class Solution {
public:
    int reverse(int x) {
        string pre;
        pre = (x < 0) ? "-" : "";
        // 没有python那种语法糖 不可以if...else...
        int temp;
        long long y, xx;
        xx = x;
        // 先转化为long long的类型 再进行运算
        y = (xx > 0) ? xx : -xx;
        long long res = 0;
        // 不可以声明为int去做后面的运算 这样可能会导致溢出
        int result;
        while (y > 0) {
            temp = y % 10;
            res = 10 * res + temp;
            y = y / 10;
        }
        if (res < INT_MIN || res > INT_MAX ) {
            // 这个就是-2**31和2**31-1 (但是C++中没有这种次方的写法)
            return 0;
        } else {
            result = (pre == "") ? res : -res;
            return result;
        }
    }
};

class Solution {
public:
    int reverse(int x) {
        long long res = 0;
        while (x != 0) {
            res = res * 10 + x % 10;
            x /= 10;
        }
        return (res < INT_MIN || res > INT_MAX) ? 0 : res;
    }
};