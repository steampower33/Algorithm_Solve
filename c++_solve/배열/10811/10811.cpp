#include <iostream>

using namespace std;

int main(void)
{
    int n, m, i, j, temp;

    cin >> n;
    cin >> m;

    int *arr = new int[n + 1];

    for (int a = 0; a < n + 1; a++)
        arr[a] = a;

    for (int a = 0; a < m; a++)
    {
        cin >> i;
        cin >> j;

        temp = 0;
        for (int b = i; b < i + (j - i + 1) / 2; b++)
        {
            temp = arr[b];
            arr[b] = arr[j + i - b];
            arr[j + i - b] = temp;
        }
    }
 
    for (int a = 1; a < n + 1; a++)
        cout << arr[a] << " ";

    return 0;
}