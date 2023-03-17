#include <iostream>

using namespace std;

int main(void)
{
	int n, m;

	cin >> n;

	m = 2;
	while (true)
	{
		if (n % m == 0)
		{
			n /= m;
			cout << m << endl;
		}
		else if(n < m)
			break;
		else
			m++;
	}
	return 0;
}