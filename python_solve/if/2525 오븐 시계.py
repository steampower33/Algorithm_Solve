
def ovenTimer(hour, minute, time):

    minutes = minute + time

    overTimes = minutes // 60
    overMinutes = minutes % 60

    if hour + overTimes >= 24:
        print(str(hour+overTimes - 24) + " " + str(overMinutes))
    else:
        print(str(hour + overTimes) + " " + str(overMinutes))

if __name__ == "__main__":
    a, b = map(int, input().split())
    c = int(input())

    ovenTimer(a,b,c)