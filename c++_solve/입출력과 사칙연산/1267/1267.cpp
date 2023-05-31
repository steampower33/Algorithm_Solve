// 1267 핸드폰 요금

#include <iostream>

using namespace std;

int bill(int I, int Y_M)
{
	int cnt;

	cnt = 0;
	while (1)
	{
		if (I < Y_M)
		{
			cnt += 1;
			break ;
		}
		I -= Y_M;
		cnt += 1;
	}
	return cnt;
}

int main(void)
{
	int N, I, Y, M;

	cin >> N;
	Y = 0;
	M = 0;
	for (int i = 0; i < N; i++)
	{
		cin >> I;
		Y += 10 * bill(I, 30);
		M += 15 * bill(I, 60);
	}
	if (Y < M)
	{
		cout << "Y " << Y << endl;
	}
	else if (Y > M)
	{
		cout << "M " << M << endl;
	}
	else if (Y == M)
	{
		cout << "Y M " << Y << endl;
	}
	return 0;
}