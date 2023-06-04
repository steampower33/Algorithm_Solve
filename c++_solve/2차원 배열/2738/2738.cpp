#include <iostream>

using namespace std;

int main(void)
{
    int n, m;

    cin >> n >> m;
    int **arr_a = new int*[n];
    for (int i = 0; i < n; i++)
        arr_a[i] = new int[m];
    int **arr_b = new int*[n];
    for (int i = 0; i < n; i++)
        arr_b[i] = new int[m];
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cin >> arr_a[i][j];
        }
    }
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cin >> arr_b[i][j];
        }
    }
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cout << arr_a[i][j] + arr_b[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}