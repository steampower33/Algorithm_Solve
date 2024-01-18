#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int climbStairs(int n) {
        vector<int> dp(n + 1, -1);
        return solve(n, dp);
    }

    int solve (int n, vector<int>& dp) {
        if (n < 0) return 0;
        if (n == 0) return 1;

        if (dp[n] != -1) return dp[n];
        
        dp[n] = solve(n - 1, dp) + solve(n - 2, dp);

        return dp[n];
    }

};

int main() {
    Solution s;

    cout << s.climbStairs(10) << endl;
}