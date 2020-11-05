#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

int main(){
    int n;
    vector<int> fibo;
    fibo.push_back(0);
    fibo.push_back(1);
    scanf("%d",&n);

    for(int i = 0; i < n-1; i++){
        fibo.push_back(fibo[fibo.size() - 2] + fibo[fibo.size() - 1]);
    }

    // for(vector<int>::iterator itr = fibo.begin(); itr < fibo.end(); itr++){
    //     printf("%d\n", *itr);
    // }
    printf("%d\n", fibo[n]);
}