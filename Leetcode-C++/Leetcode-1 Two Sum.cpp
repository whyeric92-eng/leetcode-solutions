#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> dict;
        for (int i=0; i < nums.size(); i++) {
            int temp = target - nums[i];
            if (dict.count(temp)) {
                // c++判断是不是某个字典的key的办法: dict.count(key)
                return {i,dict[temp]};
                // c++的构成数组的方式 不可以用[]
            } else {
                dict[nums[i]]=i;
            }
        }
        return {};
    }
};