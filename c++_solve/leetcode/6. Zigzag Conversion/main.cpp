#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    string convert(string s, int numRows) {
        int len = s.size();
		if (numRows <= 1) return s;
		vector<string> v(numRows, "");

		int j = 0, dir = -1;
		for (int i = 0; i < len; i++)
		{
			if (j == 0 || j == numRows - 1)
				dir *= -1;
			v[j] += s[i];

			if (dir == 1) j++;
			else j--;
		}

		string res;
		for (auto &it : v) res += it;
        return res;
    }
};

int main(void)
{
	Solution s;
	string s1;
	int numRows;

	s1 = "PAYPALISHIRING", numRows = 4;
	cout << s.convert(s1, numRows) << endl;
}