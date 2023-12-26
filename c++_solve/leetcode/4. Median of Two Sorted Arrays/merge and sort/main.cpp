#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        vector<int> r;
		int r_len;
        int mid;

        for (int i = 0; i < nums1.size(); i++)
            r.push_back(nums1[i]);
        for (int i = 0; i < nums2.size(); i++)
            r.push_back(nums2[i]);
        
        sort(r.begin(), r.end());
		r_len = nums1.size() + nums2.size();

		if (r_len % 2 == 1)
			return static_cast<double>(r[r_len / 2]);
		else
		{
			int mid1 = r[r_len / 2 - 1];
			int mid2 = r[r_len / 2];
			return (static_cast<double>(mid1) + static_cast<double>(mid2)) / 2.0;
		}
    }
};

int main(void)
{
	vector<int> num1 = {1, 2, 3, 4, 5, 6, 7};
	vector<int> num2 = {100, 102, 103};
	Solution s;

	cout << s.findMedianSortedArrays(num1, num2) << endl;
}