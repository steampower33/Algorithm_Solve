#include <iostream>
#include <vector>

using namespace std;

void get_max(int N, int M, long long *result, vector <vector <pair<long long, long long> > > &arr, vector <long long> row_max)
{
	int max_num;

	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			arr[i][j].second = row_max[i];
			max_num = 0;
			// 같은 열
			for (int k = 0; k < N; k++)
			{
				if (arr[k][j].first > arr[i][j].second)
					arr[i][j].second = arr[k][j].first;
			}
			if (arr[i][j].first >= arr[i][j].second)
				*result += 1;
		}
	}
}

void renewal_max(int N, int M, int r, int c, int x, long long *result, vector <vector <pair<long long, long long> > > &arr)
{
	// 행
	for (int i = 0; i < M; i++)
	{
		if (i == c)
			continue;
		if (arr[r][i].first >= arr[r][i].second)
			*result -= 1;
		if (arr[r][i].second < x)
			arr[r][i].second = x;
		if (arr[r][i].first >= arr[r][i].second)
			*result += 1;
		// cout << "arr : " << arr[r][i] << " " << "max_arr : " << max_arr[r][i] << " " << "result : " << *result << endl;
	}
	for (int i = 0; i < N; i++)
	{
		if (i == r)
			continue;
		if (arr[i][c].first >= arr[i][c].second)
			*result -= 1;
		if (arr[i][c].second < x)
			arr[i][c].second = x;
		if (arr[i][c].first >= arr[i][c].second)
			*result += 1;
	}
}

int main(int argc, char** argv)
{
	int test_case, T, N, M, Q, r, c;
	long long result, cnt, x, max_num;
	vector <vector <pair<long long, long long> > > arr;
	vector <long long> row_max;

	cin >> T;
	for (test_case = 1; test_case <= T; ++test_case)
	{
		cnt = 0;
		result = 0;
		cin >> N >> M >> Q;
		for (int i = 0; i < N; i++)
		{
			max_num = 0;
			vector<pair<long long, long long> > v(M);
			arr.push_back(v);
			for (int j = 0; j < M; j++)
			{
				cin >> arr[i][j].first;
				arr[i][j].second = 0;
				if (arr[i][j].first >= max_num)
					max_num = arr[i][j].first;
			}
			row_max.push_back(max_num);
		}
		get_max(N, M, &result, arr, row_max);
		// cout << "안전한 구역 개수 : " << result << endl;
		for (int i = 0; i < Q; i++)
		{
			cin >> r >> c >> x;
			if (arr[r - 1][c - 1].first >= arr[r - 1][c - 1].second)
				result -= 1;
			arr[r - 1][c - 1].first = x;
			if (arr[r - 1][c - 1].second < x)
				arr[r - 1][c - 1].second = x;
			if (arr[r - 1][c - 1].first >= arr[r - 1][c - 1].second)
				result += 1;
			renewal_max(N, M, r - 1, c - 1, x, &result, arr);
			cnt += result;
		}
		cout << "#" << test_case << " " << cnt << "\n";
		arr.clear();
		row_max.clear();
	}
	return 0;
}