#include <iostream>
#include <unordered_set>

using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
		unordered_set<char> charSet;
		int left = 0;
		int	maxLength = 0;

        for (int right = 0; right < s.size(); right++)
		{
			if (charSet.count(s[right]) == 0)
			{	
				charSet.insert(s[right]);
				maxLength = max(maxLength, right - left + 1);
			}
			else
			{
				while (charSet.count(s[right]))
				{
					charSet.erase(s[left]);
					left++;
				}
				charSet.insert(s[right]);
			}
		}
		return maxLength;
    }
};

int main(void)
{
	Solution s;
	string s1;

	s1 = "abcabcbb";
	cout << s.lengthOfLongestSubstring(s1) << endl;
	s1 = "bbbbb";
	cout << s.lengthOfLongestSubstring(s1) << endl;
	s1 = "pwwkew";
	cout << s.lengthOfLongestSubstring(s1) << endl;
}