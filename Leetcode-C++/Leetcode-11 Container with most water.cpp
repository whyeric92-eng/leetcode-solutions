#include <string>
#include <vector>
using namespace std;
class Solution {
public:
    int maxArea(vector<int>& height) {
        int result = 0, left = 0, right = height.size()-1, length = height.size()-1;
        while (left < right) {
            length = right - left;
            result = max(result, min(height[left], height[right]) * length);
            if (height[left] < height[right]) {
                left += 1;
            } else {
                right -= 1;
            }
        }
        return result;
    }
};