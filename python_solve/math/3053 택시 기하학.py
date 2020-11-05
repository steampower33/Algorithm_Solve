import math

if __name__ == "__main__":
    r = int(input())

    euclid = round(math.pi * ( r ** 2 ), 6)
    taxi = 2 * ( r ** 2 )

    print(euclid)
    print(taxi)