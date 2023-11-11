#include <iostream>
#include <cmath>

using namespace std;

int main(int argc, char** argv)
{
	int test_case;
	int T;
	int num;
	int result;
	int base_num[1001];
	int	n;

	n = 2;
	for (int i = 1; i < 1001; i++)
	{
		if (i >= n * n)
			n++;
		base_num[i] = n - 1;
		cout << i << " " << base_num[i] << endl;
	}
	cin>>T;
	for(test_case = 1; test_case <= T; ++test_case)
	{
		result = 0;
		cin >> num;
		for (int i = 1; i < base_num[num] + 1; i++)
		{
			if (num * base_num[num] == i * i)

		}
		// cout << "#" << test_case << " " << result << endl;
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}