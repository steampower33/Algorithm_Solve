// 11328 Strfry

#include <iostream>
#include <algorithm>

using namespace std;

int main(void)
{
	int N;
	string str1, str2;

	cin >> N;

	for (int i = 0; i < N; i++)
	{
		cin >> str1 >> str2;
		sort(str1.begin(), str1.end());
		sort(str2.begin(), str2.end());
		if (str1 == str2)
			cout << "Possible" << endl;
		else if (str1 != str2)
			cout << "Impossible" << endl;
	}
	return 0;
}