// 2490 윷놀이

#include <iostream>

using namespace std;

int main(void)
{
	int a, b, c, d;
	char yutnori[] = "DCBAE";

	for (int i = 0; i < 3; i++)
	{
		cin >> a >> b >> c >> d;
		cout << yutnori[(a + b + c + d)] << endl;
	}
	return 0;
}
