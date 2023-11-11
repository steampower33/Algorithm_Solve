#include <iostream>
#include <cmath>

using namespace std;

int main(int argc, char** argv)
{
	int test_case;
	int T;
	int min, max;
	int num;
	double result;

	cin>>T;
	for(test_case = 1; test_case <= T; ++test_case)
	{
		min = 10000;
		max = 0;
		result = 0;
		for (int i = 0; i < 10; i++)
		{
			cin >> num;
			if (min > num)
				min = num;
			if (max < num)
				max = num;
			result += num;
		}
		result -= (min + max);
		cout << "#" << test_case << " " << round(result / 8) << endl;
	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}