#include <iostream>
#include <cstdio>
using namespace std;

int main(){
    int x;
    int dp[1000001] = {0};
    scanf("%d", &x);

    for(int i = 2; i <= x; i++){
        dp[i] = dp[i - 1] + 1;
        if(i % 2 == 0) dp[i] = min(dp[i], dp[i / 2] + 1);
        if(i % 3 == 0) dp[i] = min(dp[i], dp[i / 3] + 1);
    }

    printf("%d",dp[x]);
    
    return 0;
}