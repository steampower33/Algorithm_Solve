#include "cpp.hpp"

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
		unordered_map<int, int> numMap;
		int len = nums.size();

		for (int i = 0; i < len; i++)
			numMap[nums[i]] = i;
		for (int i = 0; i < len; i++)
		{
			int complement = target - nums[i];
			if (numMap.count(complement) && numMap[complement] != i)
				return {i, numMap[complement]};
		}
		return {};
    }
};

int main(void)
{
	Solution s;
	vector v = {1, 2, 3, 4};
	vector<int> result;

	result = s.twoSum(v, 6);
	cout << result[0] << " " << result[1] << endl;
}