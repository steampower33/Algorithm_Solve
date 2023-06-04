// 11931 수 정렬하기 4

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(void)
{
	int N, num;
	vector<int> v;

	cin >> N;

	for (int i = 0; i < N; i++)
	{
		cin >> num;
		v.push_back(num);
	}

	sort(v.begin(), v.end());

	for (int i = N - 1; i >= 0; i--)
		cout << v[i] << endl;
	return 0;
}