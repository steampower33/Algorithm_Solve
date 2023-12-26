#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
		int n = nums1.size();
		int m = nums2.size();
		int i = 0, j = 0, min1 = 0, min2 = 0;

		for (int idx = 0; idx <= (n + m) / 2; idx++)
		{
			min2 = min1;
			if (i != n && j != m)
			{
				if (nums1[i] > nums2[j])
					min1 = nums2[j++];
				else
					min1 = nums1[i++];
			}
			else if (i < n)
				min1 = nums1[i++];
			else
				min1 = nums2[j++];
		}
		if ((n + m) % 2 == 1)
			return (static_cast<double>(min1));
		else
			return (static_cast<double>(min1) + static_cast<double>(min2)) / 2.0;
    }
};

int main(void)
{
	Solution s;
	vector<int> num1 = {4, 5, 6};
	vector<int> num2 = {1, 2, 3};

	cout << s.findMedianSortedArrays(num1, num2) << endl;
}