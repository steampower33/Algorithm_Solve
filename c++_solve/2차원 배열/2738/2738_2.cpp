#include <iostream>

using namespace std;
#define REP(v, c) for(int v = 0; v < (c); v++)

int main(void)
{
    int n, m, arr[100][100], temp;

    cin >> n >> m;
    REP(i, n)
    {
        REP(j, m)
        {
            cin >> arr[i][j];
        }
    }
    REP(i, n)
    {
        REP(j, m)
        {
            cin >> temp;
            arr[i][j] += temp;
            cout << arr[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}