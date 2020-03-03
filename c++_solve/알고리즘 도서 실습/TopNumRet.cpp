#include <iostream>
#include <vector>
#include <time.h>
#include <cstdlib>
#include <ctime>

using namespace std;
// 주어진 배열A에서 가장 많이 등장하는 숫자를 반환한다.
// 만약 두 가지 이상 있을 경우 아무것이나 반환한다.

// O(N^2)
int majority1(const vector<int>& A){
    int N = A.size();
    int majority = -1, majorityCount = 0;
    for(int i = 0; i < N; ++i){
        //A에 등장하는 A[i]의 수를 센다.
        int V = A[i], count = 0;
        for(int j = 0; j < N; ++j){
            if(A[j] == V){
                ++count;
            }
        }
        //지금까지 본 최대 빈도보다 많이 출현했다면 답을 갱신한다.
        if(count > majorityCount){
            majorityCount = count;
            majority = V;
        }
    }
    return majority;
}

// O(N)
int majority2(const vector<int>& A){
    int N = A.size();
    vector<int> count(101, 0);
    for(int i = 0; i < N; ++i){
        count[A[i]]++;
    }
    //지금까지 확인한 숫자 중 빈도수가 제일 큰 것을 majority에 저장한다.
    int majority = 0;
    for(int i = 1; i <=100; ++i){
        if(count[i] > count[majority]){
            majority = i;
        }
    }
    return majority;
}

int main(){
    clock_t start, end;
    vector<int> v;
    int result1 = 0;
    int result2 = 0;

    srand((unsigned int)time(NULL));
    for(int i = 0; i < 100; i++){
        v.push_back((rand() % 100) + 1);
    }

    start = clock();
    result1 = majority1(v);
    end = clock();
    cout << (double)(end - start) << endl;

    start = clock();
    result2 = majority2(v);
    end = clock();
    cout << (double)(end - start) << endl;

    return 0;
}