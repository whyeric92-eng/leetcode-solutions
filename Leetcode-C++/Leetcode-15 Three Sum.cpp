#include <vector>
#include <algorithm>
using namespace std;
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        int n = int(nums.size()), temp, left, right;
        vector<vector<int>> res;
        sort(nums.begin(), nums.end());

        for (int i = 0; i < n-2; i++) {
            if (i > 0 && nums[i] == nums[i-1]) {
                continue;
            }
            temp = -nums[i];
            left = i+1, right = n-1;
            while (left < right) {
                if (nums[left] + nums[right] == temp) {
                    res.push_back({nums[i], nums[left], nums[right]});
                    while (left < right && nums[left+1] == nums[left]) {
                        left += 1;
                    }
                    left += 1;
                    while (left < right && nums[right-1] == nums[right]) {
                        right -= 1;
                    }
                    right -= 1;
                } else if (nums[left] + nums[right] > temp) {
                    right -= 1;
                } else {
                    left += 1;
                }
            }
        }
        return res;
    }
};