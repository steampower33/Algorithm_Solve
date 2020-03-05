#include <iostream>
#include <cmath>
using namespace std;

int main(){
    int n = 0, num = 0, Max = 0, dp[10001] = {0}, wine[10001] = {0};

    scanf("%d", &n);

    for(int i = 1; i <= n; i++){
        scanf("%d", &num);
        wine[i] = num;
    }

    dp[1] = wine[1];
    dp[2] = wine[1] + wine[2];

    for(int i = 3; i <= n; i++){
        dp[i] = max(dp[i - 2] + wine[i], dp[i - 3] + wine[i - 1] + wine[i]);
        dp[i] = max(dp[i], dp[i-1]);
    }

    for(int i = 0; i <= n; i++){
        if(Max < dp[i]) Max = dp[i];
    }

    printf("%d", Max);

    return 0;
}