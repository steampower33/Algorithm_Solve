#include <iostream>
#include <vector>
#include <map>

using namespace std;

int main(int argc, char** argv)
{
	int test_case, T, N, M, X, Y, C, cost;
	map<int, vector<pair<int, int> > > m;

	cost = 0;
	cin >> T;
	for (test_case = 1; test_case <= T; ++test_case)
	{
		cin >> N >> M;
		for (int i = 0; i < N; i++)
		{
			vector<pair<int, int> > v;
			m[i + 1] = v;
		}
		for (int i = 0; i < M; i++)
		{
			cin >> X >> Y >> C;
			// m[X].push_back(make_pair(Y, C));
			// cout << m[0][0].first << " " << m[0][0].second << endl;
		}

	}
	return 0;
}

/*
1 2 1
1 3 5

2 1 1
2 3 1

3 2 1



*/