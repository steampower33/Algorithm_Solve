#include <iostream>

using namespace std;

#define REP(v, c) for(int v = 0; v < (c); v++)

int main(void)
{
    char arr[5][15];
    string temp;
    REP(i, 5)
    {
        REP(j, 15)
            arr[i][j] = 0;
    }
    REP(i, 5)
    {
        cin >> temp;
        REP(j, temp.length())
            arr[i][j] = temp[j];
    }
    
    REP(i, 15)
    {
        REP(j, 5)
        {
            if (arr[j][i] != 0)
                cout << arr[j][i];
        }
    }
    return 0;
}