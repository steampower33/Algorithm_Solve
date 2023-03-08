// 10813 공 바꾸기
#include <iostream>

using namespace std;

int main(void)
{
    int n, m, i, j, temp;

    cin >> n;
    cin >> m;

    int *arr = new int[n + 1];
    for(int k = 1; k < n + 1; k++)
        arr[k] = k;
    for(int k = 0; k < m; k++)
    {
        cin >> i;
        cin >> j;
        temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
    for(int k = 1; k < n + 1; k++)
        cout << arr[k] << " ";
    return 0;
}