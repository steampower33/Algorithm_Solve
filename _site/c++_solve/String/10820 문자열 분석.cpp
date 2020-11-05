#include <iostream>
#include <cstdio>
#include <string>
using namespace std;

int main(){
    for(int n = 0; n < 100; n++){
        string s;
        int lower = 0, upper = 0, num = 0, space = 0;
        getline(cin, s);
        for (int i = 0; i < s.length(); i++)
        {
            if (s[i] >= 'a' && s[i] <= 'z')
                lower++;
            else if (s[i] >= 'A' && s[i] <= 'Z')
                upper++;
            else if (s[i] >= '0' && s[i] <= '9')
                num++;
            else if (s[i] == ' ')
                space++;
        }
        if(lower == 0 && upper == 0 && num == 0 && space == 0)
            break;

        printf("%d %d %d %d\n", lower, upper, num, space);
    }
    return 0;

}