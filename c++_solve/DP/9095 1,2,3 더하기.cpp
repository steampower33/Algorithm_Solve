#include <iostream>
using namespace std;

int main(){
    int t = 0, i = 0, n = 0;
    cin >> t;
    int memo[12] = {0};
    memo[1] = 1;
    memo[2] = 2;
    memo[3] = 4;
    for(i = 4; i < 12; i++){
        memo[i] = memo[i-1] + memo[i-2] + memo[i-3];
    }
    for(i = 0; i < t; i++){
        cin >> n;
        cout << memo[n] << "\n";
    }
    return 0;
}