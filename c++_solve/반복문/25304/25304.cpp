// 25304 영수증
#include <iostream>

using namespace std;

int main(void)
{
    int x, n, a, b, total_price;

    cin >> x;
    cin >> n;
    total_price = 0;
    for (int i = 0; i < n; i++)
    {
        cin >> a;
        cin >> b;
        total_price += a * b;
    }
    if (x == total_price)
        cout << "Yes" << endl;
    else
        cout << "No" << endl;

    return 0;
}