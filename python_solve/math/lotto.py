from random import randint

def lotto1():
    lotto = list()

    for i in range(6):
        num = randint(1, 45)
        if num not in lotto:
            lotto.append(num)

    return lotto

if __name__ == "__main__":

    while True:
        num1 = lotto1()
        num2 = lotto1()

        if num1 == num2:
            print(num1)
            break