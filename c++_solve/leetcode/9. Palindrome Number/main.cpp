#include <iostream>
#include <cmath>

using namespace std;

class Solution {
public:
    bool isPalindrome(int x) {
        int len = getLength(x);
		int idx = 0;
		int num = 0;

		if (x < 0)
			return false;
		while (idx != (len / 2))
		{
			if (num < INT_MIN / 10 || num > INT_MAX / 10)
				break ;
			num *= 10;
			num += (x % 10);
			x = x / 10;
			idx++;
		}
		if (len % 2 == 1)
		{
			if (num == (x / 10))
				return true;
		}
		else
		{
			if (num == x)
				return true;
		}
		return false;
    }

	int getLength(int x)
	{
		int len = 0;
		while (x)
		{
			x /= 10;
			len++;
		}
		return len;
	}
};

int main()
{
	Solution s;
	cout << s.isPalindrome(-121) << endl;
}