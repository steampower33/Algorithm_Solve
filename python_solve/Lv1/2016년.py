def solution(a, b):
    answer = ''

    days = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    week = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    d = 0
    for _ in range(1, a):
        d += days[_]
    d += b-1

    return week[d % 7]