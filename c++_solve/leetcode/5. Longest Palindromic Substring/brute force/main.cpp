#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    string longestPalindrome(string s) {
		int max_len;
		string max_str;

		if (s.length() == 1)
			return (s);
		max_len = 1;
		max_str = s.substr(0, 1);
		for (int i = 0; i < s.length(); i++)
		{
			for (int j = i + max_len; j <= s.length(); j++)
			{
				if (j - i > max_len && isPalindrome(s.substr(i, j - i)))
				{
					max_len = j - i;
					max_str = s.substr(i, j - i);
				}
			}
		}
		return (max_str);
    }
private:
	bool isPalindrome(const string& str)
	{
		int left = 0;
		int right = str.length() - 1;

		while (left < right)
		{
			if (str[left] != str[right])
				return false;
			++left;
			--right;
		}
		return true;
	}
};

int main(void)
{
	Solution sol;

	cout << sol.longestPalindrome("aabbb") << endl;
}