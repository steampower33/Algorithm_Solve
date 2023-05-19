// 2752 세수정렬

#include <iostream>

using namespace std;

int main(void)
{
	int a, b, c, arr[3], tmp;

	cin >> a >> b >> c;
	arr[0] = a;
	arr[1] = b;
	arr[2] = c;
	
	for (int i = 0; i < 3; i++)
	{
		for (int j = i + 1; j < 3; j++)
		{
			if (arr[i] > arr[j])
			{
				tmp = arr[i];
				arr[i] = arr[j];
				arr[j] = tmp;
			}
		}
	}
	cout << arr[0] << " " << arr[1] << " " << arr[2] << endl;
	return 0;
}