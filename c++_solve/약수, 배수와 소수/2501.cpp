#include <iostream>

using namespace std;

int main(void)
{
	int n, k, cnt;

	cin >> n >> k;

	cnt = 0;
	for (int i = 1; i < n + 1; i++)
	{
		if (n % i == 0)
		{
			cnt++;
		}
		if (cnt == k)
		{
			cout << i << endl;
			return 0;
		}
	}
	cout << 0 << endl;
	return 0;
}