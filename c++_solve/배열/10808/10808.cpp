// 10808 알파벳 개수

#include <iostream>

using namespace std;

int main(void)
{
	int alpha[26];
	string str;

	cin >> str;
	for (int i = 0; i < 26; i++)
		alpha[i] = 0;

	for (int i = 0; i < str.length(); i++)
		alpha[(int)str[i] - 97] += 1;

	for (int i = 0; i < 26; i++)
		cout << alpha[i] << " ";
	cout << endl;
	return 0;
}