#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    int n = 0, sum = 0;
    int dp[101][10] = { 0,};
    for(int i = 1; i < 10; i++)
        dp[0][i] = 1;

    cin >> n;

    for(int i = 1; i < n; i++){
        for(int j = 0; j < 10; j++){
            if(j == 0)
                dp[i][j] = dp[i - 1][1];
            else if(j == 9)
                dp[i][j] = dp[i - 1][8];
            else
                dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1]) % 1000000000;
        }
    }

    // for(int i = 0; i < 4; i++){
    //     for (int j = 0; j < 10; j++){
    //         cout << dp[i][j] << " ";
    //     }
    //     cout << endl;
    // }
        

    for(int i = 0; i < 10; i++){
        sum = (sum + dp[n-1][i]) % 1000000000;
    }

    cout << sum << "\n";
    
    return 0;

}