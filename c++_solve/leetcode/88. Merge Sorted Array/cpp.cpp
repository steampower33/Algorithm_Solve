#include "cpp.hpp"

class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
		int idx;
		int tmp;

		idx = 0;
		for (int i = m; i < nums1.size(); i++)
		{
			if (nums1[i] == 0)
			{
				nums1[i] = nums2[idx];
				idx++;
			}
		}
		for (int i = 0; i < nums1.size(); i++)
		{
			for (int j = i + 1; j < nums1.size(); j++)
			{
				if (nums1[i] > nums1[j])
				{
					tmp = nums1[i];
					nums1[i] = nums1[j];
					nums1[j] = tmp;
				}
			}
		}
    }
};

int main(void)
{
	Solution s;
	vector<int> nums1 = {1, 3, 5, 7, 8, 0, 0, 0, 0};
	vector<int> nums2 = {4, 9, 11, 13};
	int m = 3;
	int n = 3;

	s.merge(nums1, m, nums2, n);
	for (int i = 0; i < nums1.size(); i++)
	{
		cout << nums1[i] << " ";
	}
	cout << endl;
}