// 2309 일곱 난쟁이

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool stop = false;

void Combination(int d[], vector<int> comb, int r, int idx, int depth)
{
	int max;

	if (stop == true)
		return ;
	if (r == 0)
	{
		max = 0;
		for (int i = 0; i < 7; i++)
			max += comb[i];
		if (max == 100)
		{
			sort(comb.begin(), comb.end());
			for (int i = 0; i < 7; i++)
				cout << comb[i] << endl;
			stop = true;
		}
	}
	else if (depth == 9)
	{
		return ;
	}
	else
	{
		comb[idx] = d[depth];
		Combination(d, comb, r - 1, idx + 1, depth + 1);
		Combination(d, comb, r, idx, depth + 1);
	}
}

int main(void)
{
	int dwarf[9], r, flag;

	for (int i = 0; i < 9; i++)
		cin >> dwarf[i];
	r = 7;
	vector<int> comb(r);

	Combination(dwarf, comb, r, 0, 0);	
	return 0;
}