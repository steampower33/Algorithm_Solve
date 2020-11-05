#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

int main(int argc, char * argv[]){
    int n = 0, v = 0, num = 0, nums[201];

    cin >> n;
    memset(nums, 0, sizeof(nums));

    for(int i = 0; i < n; ++i){
        cin >> num;
        ++nums[num+100];
    }

    cin >> v;

    cout << nums[v+100] << endl;

    return 0;
}