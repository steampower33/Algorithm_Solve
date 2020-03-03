#include <iostream>
#include <vector>
#include <time.h>

using namespace std;

// O(N^2)
//실수 배열 A가 주어질때, 각 위치에서의 M-이동 평균 값을 구한다.
vector<double> movingAverage1(const vector<double>& A, int M){
    vector<double> ret;
    int N = A.size();
    for(int i = M-1; i < N; ++i){
        //A[i]까지의 이동 평균 값을 구하자.
        double partialSum = 0;
        for(int j = 0; j < M; ++j)
            partialSum += A[i-j];
        ret.push_back(partialSum / M);
    }
    return ret;
}

// O(N)
// 길이가 N인 실수 배열 A가 주어질 때, 각 위치에서의 M-이동 평균 값을 구한다.
vector<double> movingAverage2(const vector<double>& A, int M){
    vector<double> ret;
    int N = A.size();
    double partialSum = 0;
    for(int i = 0; i < M-1; ++i)
        partialSum += A[i];
    for(int i = M-1; i < N; ++i){
        partialSum += A[i];
        ret.push_back(partialSum / M);
        partialSum -= A[i-M+1];
    }
    return ret;
}

int main(){
    clock_t start, end;
    vector<double> value;
    for(int i = 0; i < 100; ++i){
        int in = i*2 + 3;
        value.push_back(in);
    }
    start = clock();
    vector<double> ret1 = movingAverage1(value, 50);
    end = clock();
    cout << (double)(end - start) << endl;
    
    start = clock();
    vector<double> ret2 = movingAverage2(value, 50);
    end = clock();
    cout << (double)(end - start) << endl;
    return 0;
} 