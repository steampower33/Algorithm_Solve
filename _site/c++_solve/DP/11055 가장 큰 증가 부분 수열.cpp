#include <iostream>
using namespace std;

int main(){
    int n = 0, a = 0, max_num = 0, dp[1001] = {0}, sequence[1001] = {0};
    cin >> n;

    for(int i = 1; i <= n; i++){
        cin >> a;
        sequence[i] = a;
    }

    for(int i = 1; i <= n; i++){
        dp[i] = sequence[i];
        for(int j = 1; j < i; j++){
            if( sequence[j] < sequence[i] && dp[i] < dp[j] + sequence[i])
                dp[i] = dp[j] + sequence[i];
        }
    }

    for(int i = 0; i <= n; i++){
        if( max_num < dp[i] )
            max_num = dp[i];
    }

    cout << max_num << "\n";
    
    return 0;
}