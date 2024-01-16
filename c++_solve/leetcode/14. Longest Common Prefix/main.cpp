#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
		if (strs.empty()) return "";
		size_t pos;
		string prefix = strs[0];
		for (string s : strs)
		{
			while (s.find(prefix) != 0)
				prefix = prefix.substr(0, prefix.size() - 1);
		}
		return prefix;
    }
};

int main() {
	Solution s;
	vector<string> strs = {"flower","flow","flight"};

	cout << s.longestCommonPrefix(strs) << endl;
}