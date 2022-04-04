class Solution:
    def fib(self, n: int) -> int:
        fibo = [0 for _ in range(n+1)]

        if n == 0:
            fibo[0] = 0
        else:
            fibo[0] = 0
            fibo[1] = 1

        for _ in range(2, n+1):
            fibo[_] = fibo[_-1] + fibo[_-2]

        return fibo[n]