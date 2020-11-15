
def fibonacci(n):
    for i in range(2, n+1):
        fibo[i] = fibo[i-2] + fibo[i-1]

if __name__ == "__main__":
    n = int(input())
    fibo = [0 for i in range(n+1)]
    fibo[0] = 0
    fibo[1] = 1

    fibonacci(n)

    print(fibo[n])