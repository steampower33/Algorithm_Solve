#include <iostream>

using namespace std;

#define REP(v, v_min, c) for(int v=v_min; v<(c); v++)

int main(void)
{
    int matrix[100][100], n, x, y, cnt;

    cin >> n;

    REP(i, 0, 100)
    {
        REP(j, 0, 100)
            matrix[i][j] = 0;
    }

    REP(i, 0, n)
    {
        cin >> x >> y;

        REP(j, y, y+10)
        {
            REP(k, x, x+10)
            {
                matrix[j][k] = 1;
            }
        }
    }

    cnt = 0;
    REP(i, 0, 100)
    {
        REP(j, 0, 100)
        {
            if (matrix[i][j] == 1)
                cnt++;
        }
    }
    cout << cnt << endl;
    return 0;
}