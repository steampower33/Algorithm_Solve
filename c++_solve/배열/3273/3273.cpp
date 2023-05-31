// 3273 두 수의 합

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(void)
{
	int n, num, x, cnt, end;
	vector<int> nums;

	cin >> n;
	for (int i = 0; i < n; i++)
	{
		cin >> num;
		nums.push_back(num);
	}
	cin >> x;
	sort(nums.begin(), nums.end());
	cnt = 0;
	for (int start = 0; start < n - 1; start++)
	{
		end = start + 1;
		while (nums[start] + nums[end] < x && end < n)
		{
			end += 1;
		}
		if (nums[start] + nums[end] == x)
			cnt += 1;
	}
	cout << cnt << endl;
	return 0;
}