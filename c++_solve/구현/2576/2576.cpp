// 2576 홀수
#include <iostream>

using namespace std;

int main(void)
{
	int m, s, input;

	s = 0;
	m = 0;
	for (int i = 0; i < 7; i++)
	{
		cin >> input;
		if (input % 2 == 1)
		{
			s += input;
			if (m == 0)
				m = input;
			else if (input < m)
				m = input;
		}
	}
	if (s == 0)
		cout << "-1" << endl;
	else
	{
		cout << s << endl;
		cout << m << endl;
	}
	return 0;
}
