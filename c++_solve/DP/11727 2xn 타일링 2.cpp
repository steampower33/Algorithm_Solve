#include <iostream>
using namespace std;

int main(){
    int n = 0;
    cin >> n;
    int squares[1001] = {0};
    squares[1] = 1;
    squares[2] = 3;
    for(int i = 3; i < n+1; i++){
        squares[i] = (squares[i-1] + squares[i-2]*2) % 10007;
    }

    cout << squares[n] << endl;
    return 0;
}