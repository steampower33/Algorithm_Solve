#include <iostream>

using namespace std;

int main(void)
{
	int n, matrix[50000], cnt, sum;

	n = 0;
	while (true)
	{
		cin >> n;
		cnt = 0;
		sum = 0;
		for (int i = 1; i < n / 2 + 1; i++)
		{
			if (n % i == 0)
			{
				cnt++;
				matrix[cnt] = i;
			}
		}

		for (int i = 1; i < cnt + 1; i++)
			sum += matrix[i];
		if (n == sum)
		{
			cout << n << " = ";
			for (int i = 1; i < cnt + 1; i++)
			{
				cout << matrix[i];
				if (i != cnt)
					cout << " + ";
			}
			cout << endl;
		}
		else if (n == -1)
			break;
		else
			cout << n << " is NOT perfect." << endl;
	}
}