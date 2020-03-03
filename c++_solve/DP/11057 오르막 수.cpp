#include <iostream>
using namespace std;

int main() {
    int n = 0, sum = 0;
    cin >> n;
    int dp[1001][10] = { 0,};

    for(int i = 0; i < 10; i++){
        dp[1][i] = 1;
    }

    for(int i = 2; i <= 1000; i++){
        for(int j = 9; j >= 0; j--){
            if( j == 9 ) {
                dp[i][j] = 1;
            }
            else if( j == 8) {
                dp[i][j] = i;
            }
            else{
                dp[i][j] = (dp[i - 1][j] + dp[i][j + 1]) % 10007;
            }
        } 
    }

    for(int i = 0; i < 10; i++){
        sum = (sum + dp[n][i]) % 10007;
    }

    cout << sum << "\n";


    return 0;
}