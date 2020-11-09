
if __name__ == "__main__":
    people = list()

    n = int(input())
    for i in range(n):
        w, h = map(int, input().split())
        people.append((w,h))

    grade = [0 for i in range(len(people))]

    for i in range(len(people)):
        count = 1
        for j in range(len(people)):
            if i == j: continue
            if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
                count += 1
        grade[i] = count

    for i in grade:
        print(i, end=" ")

