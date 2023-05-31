// 1475 방 번호

#include <iostream>

using namespace std;

int main(void)
{
	string N;
	int num[10], six_nine, m;
	cin >> N;

	for (int i = 0; i < 10; i++)
		num[i] = 0;

	for (int i = 0; i < N.length(); i++)
		num[(int)N[i] - 48] += 1;
	// cout << num[6] << " " << num[9] << endl;
	six_nine = 0;
	if ((num[6] + num[9]) % 2 != 0)
		six_nine += (num[6] + num[9]) / 2 + 1;
	else
		six_nine += (num[6] + num[9]) / 2;

	// cout << six_nine << endl;

	m = 0;
	for (int i = 0; i < 10; i++)
	{
		if (i == 6 or i == 9)
			continue;
		if (m < num[i])
			m = num[i];
	}
	cout << max(m, six_nine) << endl;
	return 0;
}