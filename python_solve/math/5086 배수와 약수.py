import sys

if __name__ == "__main__":

    a, b = -1, -1
    while True:
        a, b = map(int, sys.stdin.readline().rsplit())

        if a == 0 == b == 0: break

        quotientA = a // b
        remainderA = a % b

        quotientB = b // a
        remainderB = b % a

        if quotientA != 0 and remainderA == 0:
            print("multiple")
        elif quotientB != 0 and remainderB == 0:
            print("factor")
        else:
            print("neither")