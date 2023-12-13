#include <iostream>
#include <string>
#include <map>

using namespace std;

class Solution {
public:

    int romanToInt(string s) {
		map<char, int> m;
		int result;

		m['I'] = 1;
		m['V'] = 5;
		m['X'] = 10;
		m['L'] = 50;
		m['C'] = 100;
		m['D'] = 500;
		m['M'] = 1000;
		result = 0;
		for (int i = 0; i < s.size(); i++)
		{
			if (s[i] == 'I')
			{
				if (i + 1 < s.size() && (s[i + 1] == 'V' || s[i + 1] == 'X'))
				{
					result += (m[s[i + 1]] - m[s[i]]);
					i++;
				}
				else
					result += m[s[i]];
			}
			else if (s[i] == 'X')
			{
				if (i + 1 < s.size() && (s[i + 1] == 'L' || s[i + 1] == 'C'))
				{
					result += (m[s[i + 1]] - m[s[i]]);
					i++;
				}
				else
					result += m[s[i]];
			}
			else if (s[i] == 'C')
			{
				if (i + 1 < s.size() && (s[i + 1] == 'D' || s[i + 1] == 'M'))
				{
					result += (m[s[i + 1]] - m[s[i]]);
					i++;
				}
				else
					result += m[s[i]];
			}
			else
				result += m[s[i]];
		}
		return result;
    }
};

int main(void)
{
	Solution s;
	string	in;

	in = "III";
	cout << s.romanToInt(in) << endl;
	in = "LVIII";
	cout << s.romanToInt(in) << endl;
	in = "MCMXCIV";
	cout << s.romanToInt(in) << endl;
}