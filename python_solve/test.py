
l = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)]

for i in range(len(l)):
    for j in range(i + 1, len(l)):
        if l[i][0] or l[i][1] in l[j]:
            continue
        else:
            print(0)