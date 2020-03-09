#include <iostream>
using namespace std;

int main(){
    int n = 0, k = 0, dp[201][201] = {0};

    scanf("%d %d", &n, &k);

    for(int i = 1; i <= k; i++) dp[0][i] = 1;

    for(int i = 1; i <= n; i++){
        for(int j = 1; j <= k; j++){
            dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % 1000000000;
        }
    }

    printf("%d",dp[n][k]);

    return 0;
}