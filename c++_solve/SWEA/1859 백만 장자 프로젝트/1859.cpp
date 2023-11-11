#include <iostream>
#include <vector>

using namespace std;

int main(void)
{
	long long T, N, m, num, result;
	vector<int> v;
	pair<int, int> p;

	cin >> T;
	for(int test_case = 1; test_case <= T; ++test_case)
	{
		cin >> N;
		for (int j = 0; j < N; j++)
		{
			cin >> num;
			v.push_back(num);
		}
		p = {0, 0};
		result = 0;
		for (int j = 0; j < N; j++)
		{
			if (j > 0)
			{
				if (j > p.first)
				{
					p.first = j;
					p.second = v[j];
					for (int k = j + 1; k < N; k++)
					{
						if (p.second < v[k])
						{
							p.first = k;
							p.second = v[k];
						}
					}
				}
			}
			else
			{
				p.first = j;
				p.second = v[j];
				for (int k = j + 1; k < N; k++)
				{
					if (p.second < v[k])
					{
						p.first = k;
						p.second = v[k];
					}
				}
			}
			if (v[j] < p.second)
				result += (p.second - v[j]);
		}
		cout << "#" << test_case << " " << result << endl;
		v.clear();
	}
	return 0;
}