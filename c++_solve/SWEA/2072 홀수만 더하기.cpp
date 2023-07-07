#include<iostream>

using namespace std;

int main(int argc, char** argv)
{
	int test_case;
	int T;
    int	answer;
    int	num;

	cin>>T;
	for(test_case = 1; test_case <= T; ++test_case)
	{
        answer = 0;
        num = 0;
        for (int i = 0; i < 10; i++)
        {
            cin >> num;
            if (num % 2 == 1)
                	answer += num;
        }
        cout << "#" << test_case << " " << answer << endl;
	}
	return 0;
}