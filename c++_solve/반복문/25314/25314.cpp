// 25314 코딩은 체육과목 입니다
#include <iostream>

using namespace std;

int main(void)
{
    int n;

    cin >> n;

    for (int i = 0; i < n / 4; i++)
        cout << "long ";
    cout << "int" << endl;
    return 0;
}