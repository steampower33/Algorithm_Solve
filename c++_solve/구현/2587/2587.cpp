// 2587 대표값2

#include <iostream>
#include <algorithm>

using namespace std;

int main(void)
{
	int num[5], avr, tmp;

	avr = 0;
	for (int i = 0; i < 5; i++)
	{
		cin >> num[i];
		avr += num[i];
	}
	avr /= 5;

	for (int i = 0; i < 5; i++)
	{
		for (int j = i + 1; j < 5; j++)
		{
			if (num[i] > num[j])
			{
				tmp = num[i];
				num[i] = num[j];
				num[j] = tmp;
			}
		}
	}
	cout << avr << endl;
	cout << num[2] << endl;
	return 0;
}