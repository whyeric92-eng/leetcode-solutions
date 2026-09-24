#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int n = int(nums.size());
        vector<vector<int>> res;
        // 外层不能用双指针夹逼, 只能两个 for 循环枚举 i, j:
        // 夹逼的前提是"和大了就挪右边, 和小了就挪左边", 只有剩下两个数没定时才成立
        // 外层如果也夹逼, 内层的结果没法告诉你该挪 left 还是 right, 会漏掉解
        // 所以外层 O(n^2) 固定前两个数, 内层双指针 O(n) 找后两个数, 总共 O(n^3)
        for (int i = 0; i < n - 3; i++) {
            if (i > 0 && nums[i] == nums[i-1]) continue;
            for (int j = i + 1; j < n - 2; j++) {
                if (j > i + 1 && nums[j] == nums[j-1]) continue;
                int left = j + 1, right = n - 1;
                long long temp = (long long)target - nums[i] - nums[j];
                while (left < right) {
                    long long sum = (long long)nums[left] + nums[right];
                    if (sum > temp) {
                        right -= 1;
                    } else if (sum == temp) {
                        res.push_back({nums[i], nums[j], nums[left], nums[right]});
                        while (left < right && nums[left] == nums[left+1]) {
                            left += 1;
                        }
                        while (left < right && nums[right] == nums[right-1]) {
                            right -= 1;
                        }
                        left += 1;
                        right -= 1;
                    } else {
                        left += 1;
                    }
                }
            }
        }
        return res;
    }
};
