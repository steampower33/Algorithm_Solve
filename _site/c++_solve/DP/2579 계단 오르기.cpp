#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    int n = 0, score = 0;
    int stairs[301] = {0};
    int dp[301] = {0};

    scanf("%d", &n);

    for(int i = 0; i < n; i++){
        scanf("%d", &score);
        stairs[i] = score;
    }

    dp[0] = stairs[0];
    dp[1] = max(stairs[0]+stairs[1], stairs[1]);
    dp[2] = max(stairs[0]+stairs[2], stairs[1]+stairs[2]);

    for(int i = 3; i < n; i++){
        dp[i] = max(dp[i-3] + stairs[i-1] + stairs[i], dp[i-2] + stairs[i]);
    }

    printf("%d", dp[n-1]);
    return 0;
}