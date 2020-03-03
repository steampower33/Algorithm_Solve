#include <iostream>
#include <cstdio>
using namespace std;

int main(){
    int n = 0;
    int rtn = 0;
    scanf("%d", &n);
    int squares[1001] = {0};
    squares[1] = 1; squares[2] = 2;

    for(int i = 3; i < n+1; i++){
        squares[i] = (squares[i-2] + squares[i-1]) % 10007;
    }

    printf("%d", squares[n]);
    return 0;
}