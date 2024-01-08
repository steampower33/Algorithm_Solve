#include <iostream>

class Solution {
public:
    int reverse(int x) {
		int res;

		res = 0;
        while (x)
		{
			if (res < INT_MIN / 10 || res > INT_MAX / 10)
				return 0;
			res *= 10;
			res += (x % 10);
			x = x / 10;
		}
		return res;
    }
};

int main()
{
	Solution s;

	std::cout << s.reverse(-2147) << std::endl;
}