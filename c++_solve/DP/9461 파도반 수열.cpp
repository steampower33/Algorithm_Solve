#include <iostream>
using namespace std;

int main(){
    int t = 0, n = 0;
    long long dp[101] = {0};

    cin >> t;

    dp[1] = 1;
    dp[2] = 1;

    for(int i = 3; i <=100; i++){
        dp[i] = dp[i-2] + dp[i-3];
    }

    for(int i = 0; i < t; i++){
        cin >> n;
        cout << dp[n] << "\n";
    }

    return 0;
}