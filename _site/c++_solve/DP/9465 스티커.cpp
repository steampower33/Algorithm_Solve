#include <iostream>
#include <cmath>
using namespace std;

int main(){
    int i = 0, j = 0, k = 0;
    int tc = 0, n = 0, num = 0;

    scanf("%d", &tc);

    for(i = 0; i < tc; i++){
        int stickers[2][100001] = {0}, dp[2][100001] = {0};
        scanf("%d", &n);
        for(j = 0; j < 2; j++){
            for(k = 1; k <= n; k++){
                scanf("%d", &num);
                stickers[j][k] = num;
            }
        }
        dp[0][1] = stickers[0][1];
        dp[1][1] = stickers[1][1];

        for(j = 2; j <= n; j++){
            dp[0][j] = max(dp[1][j - 1], dp[1][j - 2]) + stickers[0][j];
            dp[1][j] = max(dp[0][j - 1], dp[0][j - 2]) + stickers[1][j];
        }

        printf("%d\n",max(dp[0][n],dp[1][n]));
    }

    return 0;
}