#include <vector>
#include <algorithm>
#include <cstdlib>
using namespace std;
class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int res = nums[0] + nums[1] + nums[2], temp, n = int(nums.size()), left, right;
        for (int i = 0; i < n - 2; i++) {
            left = i+1, right = n-1;
            while (left < right) {
                temp = nums[i] + nums[left] + nums[right];
                if(abs(temp - target) < abs(res - target)) {
                // 不初始化res的话 可以用res.hasvalue()来判断
                    res = temp;
                }
                if (temp == target) {
                    return target;
                }
                if (temp > target) {
                    right -= 1;
                } else {
                    left += 1;
                }
            }
        }
        return res;
    }
};

// 剪枝版本：跳过重复元素，并利用有序数组的最小/最大三数和提前终止或跳过当前 i
class SolutionPruned {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int n = int(nums.size());
        int res = nums[0] + nums[1] + nums[2];
        for (int i = 0; i < n - 2; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }

            // 当前 i 能取到的最小三数和，若已经比 target 大，
            // 之后的 i 只会更大，直接更新答案后结束整个循环
            int minSum = nums[i] + nums[i + 1] + nums[i + 2];
            if (minSum >= target) {
                if (abs(minSum - target) < abs(res - target)) {
                    res = minSum;
                }
                break;
            }

            // 当前 i 能取到的最大三数和，若仍比 target 小，
            // 说明内层双指针不可能更优，更新答案后跳过内层循环
            int maxSum = nums[i] + nums[n - 2] + nums[n - 1];
            if (maxSum <= target) {
                if (abs(maxSum - target) < abs(res - target)) {
                    res = maxSum;
                }
                continue;
            }

            int left = i + 1, right = n - 1;
            while (left < right) {
                int temp = nums[i] + nums[left] + nums[right];
                if (abs(temp - target) < abs(res - target)) {
                    res = temp;
                }
                if (temp == target) {
                    return target;
                } else if (temp > target) {
                    right -= 1;
                    while (left < right && nums[right] == nums[right + 1]) {
                        right -= 1;
                    }
                } else {
                    left += 1;
                    while (left < right && nums[left] == nums[left - 1]) {
                        left += 1;
                    }
                }
            }
        }
        return res;
    }
};