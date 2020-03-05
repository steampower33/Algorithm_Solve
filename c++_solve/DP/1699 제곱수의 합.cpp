#include <iostream>
#include <cmath>
using namespace std;

int main(){
    int n = 0, dp[100001] = {0};
    cin >> n;
    for(int i = 0; i <= n; i++) dp[i] = i;
    for(int i = 2; i <= n; i++)
        for(int j = 2; j*j <= i; j++)
            dp[i] = min(dp[i], dp[i - j*j] + 1);
            
    cout << dp[n] << "\n";

    return 0;
}