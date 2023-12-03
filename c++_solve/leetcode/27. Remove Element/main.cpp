#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    
    int removeElement(vector<int>& nums, int val) {
		int	idx;

        idx = 0;
        for (int i = 0; i < nums.size(); i++)
        {
			if (nums[i] != val)
			{
				nums[idx] = nums[i];
				idx++;
            }
        }
		return idx;
    }
};

int main()
{
	vector<int> nums = {3,2,2,3};
	int val = 3;
	Solution s;

	int k = s.removeElement(nums, val); // Calls your implementation
	cout << k << endl;
}