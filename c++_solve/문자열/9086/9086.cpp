#include <iostream>

using namespace std;

int main(void)
{
    int t;
    string str;

    cin >> t;

    for (int i = 0; i < t; i++)
    {
        cin >> str;
        cout << str.at(0) << str.at(str.length() - 1) << endl;
    }
    return 0;
}