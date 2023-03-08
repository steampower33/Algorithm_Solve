// 5597 과제 안 내신 분..?
#include <iostream>

using namespace std;

int main(void)
{
    int arr[31], n, cnt;
    for (int i = 0; i < 31; i++)
        arr[i] = 0;

    for (int i = 0; i < 28; i++)
    {
        cin >> n;
        arr[n] = 1;
    }

    cnt = 0;
    for (int j = 1; j < 31; j++)
    {
        if (arr[j] != 1)
        {
            cout << j << endl;
            cnt++;
        }
        if (cnt == 2)
            return 0;
    }
    return 0;
}