// 2480 주사위 세개
#include <iostream>
#include <algorithm>

using namespace std;

int main(void)
{
    int a, b, c;
    cin >> a;
    cin >> b;
    cin >> c;

    if (a == b && b == c)
        cout << 10000 + a * 1000 << endl;
    else if (a == b || b == c || a == c)
        cout << (a == b) * 1000 + a * (a == b) * 100
        + (b == c) * 1000 + b * (b == c) * 100
        + (a == c) * 1000 + a * (a == c) * 100 << endl;
    else
        cout << max(max(a,b),c) * 100 << endl;
    return 0;
}