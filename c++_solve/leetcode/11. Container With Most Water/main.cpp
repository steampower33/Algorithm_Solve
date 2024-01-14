#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int maxArea(vector<int>& height) {
        int max_num = 0;
		int len = height.size();
		int left, right;

		left = 0;
		right = len - 1;
		while (left < right)
		{
			max_num = max(max_num, (right - left) * min(height[left], height[right]));
			if (height[left] <= height[right])
				left++;
			else
				right--;
		}
		return max_num;
    }
};

int main() {
	Solution s;
    std::vector<int> myVector = {1,8,6,2,5,4,8,3,7};

	cout << s. maxArea(myVector) << endl;
}