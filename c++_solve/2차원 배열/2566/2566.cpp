#include <iostream>

using namespace std;

#define REP(v, c) for(int v = 0; v < (c); v++)

int main(void)
{
    int matrix[9][9], r, c, num, m;

    m = 0;
    c = 1;
    r = 1;
    REP(i, 9)
    {
        REP(j, 9)
        {
            cin >> num;
            if (num > m)
            {
                m = num;
                c = i + 1;
                r = j + 1;
            }
        }
    }
    cout << m << endl;
    cout << c << " " << r << endl;
    return 0;
}