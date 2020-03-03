#include <iostream>
#include <cstdio>
using namespace std;

int main(){
    char c[1000000];
    int count = 0;
    scanf("%[^\n]s", c);
    //cin.getline(c, 1000000); // 문장 입력

    int space = 1;

    for(int i = 0; c[i]; i++){
        //printf("%c\n", c[i]);
        if(c[i] == ' ') space = 1;
        else if( space ){
            space = 0;
            count++;
        }
    }

    printf("%d", count);

    return 0;
}