// 10093 숫자

#include <iostream>

using namespace std;

int main(void)
{
	unsigned long long a, b, tmp;

	cin >> a >> b;

	if (a > b)
	{
		tmp = a;
		a = b;
		b = tmp;
	}
	if (a == b)
	{
		cout << b - a << endl;
		return 0;
	}
	cout << b - a - 1 << endl;
	for (unsigned long long i = a + 1; i < b; i++)
		cout << i << " ";
	cout << endl;
	return 0;
}
