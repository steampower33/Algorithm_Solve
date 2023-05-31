// 13300 방 배정

#include <iostream>
#include <vector>

using namespace std;

int main(void)
{
	int N, K, S, Y, cnt;
	vector< vector<int> > v(7, vector<int>(2,0));

	cin >> N >> K;
	for (int i = 0; i < N; i++)
	{
		cin >> S >> Y;
		v[Y][S] += 1;
	}

	cnt = 0;
	for (int i = 1; i < 7; i++)
	{
		for (int j = 0; j < 2; j++)
		{
			if (v[i][j] == 0)
				continue;
			else if (v[i][j] % K != 0)
				cnt += v[i][j] / K + 1;
			else if (v[i][j] % K == 0)
				cnt += v[i][j] / K;
		}
	}
	cout << cnt << endl;
	return 0;
}