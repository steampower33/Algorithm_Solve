//1919 애너그램 만들기

#include <iostream>

using namespace std;

int main(void)
{
	string str;
	int ascii[26], cnt;

	for (int i = 0; i < 26; i++)
		ascii[i] = 0;
	cin >> str;
	for (int i = 0; i < str.length(); i++)
	{
		ascii[(int)str[i] - 97] += 1;
	}
	cin >> str;
	for (int i = 0; i < str.length(); i++)
	{
		ascii[(int)str[i] - 97] -= 1;
	}

	cnt = 0;
	for (int i = 0; i < 26; i++)
	{
		// cout << ascii[i] << " ";
		if (ascii[i] > 0)
			cnt += ascii[i];
		else
			cnt += ascii[i] * -1;
	}
	cout << cnt << endl;
	return 0;
}