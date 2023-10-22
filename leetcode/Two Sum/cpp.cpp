#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
		vector<int> v(2, 0);

		for (int i = 0; i < nums.size(); i++)
		{
			for (int j = i + 1; j < nums.size(); j++)
			{
				if (nums[i] + nums[j] == target)
				{
					v[0] = i;
					v[1] = j;
					break ;
				}
			}
		}
		return (v);
    }
};

int main(void)
{
	Solution s;
	vector v = {1, 2, 3, 4};
	vector<int> result;

	result = s.twoSum(v, 6);
	cout << result[0] << result[1] << endl;
}