#include <vector>
#include <string>
#include <unordered_map>
using namespace std;

// 思路: 经典 backtracking(回溯)
// 每一层递归对应 digits 里的一位数字, 在该数字对应的几个字母里做选择:
//   做出选择(path += c) -> 递归进入下一层(index+1) -> 撤销选择(path.pop_back())
// 递归到 index == digits.size() 时说明 path 已经选满了每一位, 收集结果。

class Solution {
public:
    vector<string> letterCombinations(string digits) {
        if (digits.empty()) return res; // 边界: 空输入直接返回空结果
        string path;       // 必须是有名字的左值, 因为下面按 & 传给 backtracking
        backtracking(0, path, digits);
        return res;
    }
private:
    // C++ 写法细节 1:
    // C++ 不支持在函数内部再定义一个具名函数(不像 Python 可以在函数里 def 一个子函数),
    // 所以回溯用的辅助函数不能直接写在 letterCombinations 内部。
    // 常见的两种解决方式:
    //   方式 A(本文件采用): 把回溯函数写成 class 的 private 成员函数,
    //                        这样它可以直接访问同为成员的 dict / res,
    //                        但要注意 digits 不是成员变量, 需要作为参数一路传下去。
    //   方式 B: 用 lambda 表达式, 在 letterCombinations 内部定义一个递归 lambda
    //           (因为要递归调用自己, 需要 std::function 包一层, 或者 C++23 的 deducing this)。
    //           写法示例(未启用, 仅供对比):
    //
    // vector<string> letterCombinations(string digits) {
    //     if (digits.empty()) return {};
    //     vector<string> res;
    //     string path;
    //     // 递归 lambda 必须先声明类型(std::function), 再赋值, 否则 lambda 内部无法引用自己
    //     function<void(int)> backtracking = [&](int index) {
    //         if (index == (int)digits.size()) {
    //             res.push_back(path);
    //             return;
    //         }
    //         for (char c : dict[digits[index]]) {
    //             path += c;
    //             backtracking(index + 1);
    //             path.pop_back();
    //         }
    //     };
    //     backtracking(0);
    //     return res;
    // }
    //
    // lambda 方式的好处是 res / path / digits 都通过 [&] 按引用捕获, 不需要像成员函数那样
    // 显式地把 digits 当参数传递; 缺点是递归 lambda 需要 std::function 包装, 有一点额外开销,
    // 而且写法不如成员函数直观。

    unordered_map<char, vector<char>> dict = {
        {'2', {'a','b','c'}}, {'3', {'d','e','f'}}, {'4', {'g','h','i'}},
        {'5', {'j','k','l'}}, {'6', {'m','n','o'}}, {'7', {'p','q','r','s'}},
        {'8', {'t','u','v'}}, {'9', {'w','x','y','z'}}
    };
    vector<string> res;

    // C++ 写法细节 2: 值传递 vs 引用传递
    // - path 用非 const 引用传递(string& path): 整个递归树里从头到尾只有这一个 string 对象,
    //   不会像值传递那样每层递归都拷贝一份, 效率更高。正因为所有递归调用共享同一个对象,
    //   才必须手动 push_back(做选择)/pop_back(撤销选择)来维护它: 进入下一层前加上当前字母,
    //   递归返回后再删掉, 这样回到上一层/切换到下一个兄弟分支时 path 才是正确的状态。
    //   注意: 非 const 引用只能绑定到左值, 所以调用处不能直接传 "" (临时对象/右值),
    //   必须先声明一个具名的 string 变量(见 letterCombinations 里的 path)再传进来。
    // - digits 用 const 引用传递(const string&): 因为 digits 在整个递归过程中不会被修改,
    //   用引用可以避免每层递归都拷贝一次字符串, 加 const 是为了防止函数内部不小心改动它,
    //   同时也表明"这个参数只读"的意图, 而且 const 引用可以绑定右值, 传参更灵活。
    void backtracking(int index, string& path, const string& digits) {
        if (index == int(digits.size())) {
            res.push_back(path);
            return;
        }
        for (char c : dict[digits[index]]) {
            path += c;                       // 做出选择
            backtracking(index+1, path, digits); // 递归
            path.pop_back();                 // 撤销选择, 尝试下一个字母
        }
    }
};
