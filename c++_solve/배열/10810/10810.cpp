// 10810 공 넣기
#include <iostream>

using namespace std;

int main(void)
{
    int n, m, i, j, k;

    cin >> n;
    cin >> m;

    int *arr = new int[n + 1];

    for (int a = 0; a < m; a++)
    {
        cin >> i;
        cin >> j;
        cin >> k;
        for (int cnt = i; cnt < j + 1; cnt++)
            arr[cnt] = k;
    }

    for (int a = 1; a < n + 1; a++)
        cout << arr[a] << " ";

    return 0;
}