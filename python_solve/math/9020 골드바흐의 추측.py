def isPrimeNumber(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

if __name__ == "__main__":
    testCase = int(input())
    for i in range(testCase):
        n = int(input())
        lower = n // 2
        upper = n // 2
        for i in range(n // 2 + 1):
            isLowerPrime = isPrimeNumber(lower)
            isUpperPrime = isPrimeNumber(upper)

            if isLowerPrime == True and isUpperPrime == True:
                print(lower, upper)
                break

            lower -= 1
            upper += 1


