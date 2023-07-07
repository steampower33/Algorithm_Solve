#include <iostream>
#include <vector>

using namespace std;

int main(int argc, char** argv)
{
	int test_case, N, num, T, result;
	vector<int> v;

	T = 10;
	for(test_case = 1; test_case <= T; ++test_case)
	{
		result = 0;
		cin >> N;
		for(int i = 0; i < N; i++)
		{
			cin >> num;
			v.push_back(num);
		}

		for(int i = 2; i < N - 2; i++)
		{
			if(v[i] > max(max(v[i - 2], v[i - 1]), max(v[i + 1], v[i + 2])))
			{
				result += v[i] - max(max(v[i - 2], v[i - 1]), max(v[i + 1], v[i + 2]));
			}
		}
		cout << "#" << test_case << " " << result << endl;
		v.clear();
	}
	return 0;
}