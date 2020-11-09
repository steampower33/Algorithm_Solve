import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())

    words = dict()
    for i in range(1, 51):
        words[i] = list()

    for i in range(N):
        word = sys.stdin.readline().rstrip()
        if word not in words[len(word)]:
            words[len(word)].append(word)

    for i in range(1, 51):
        if not words[i]: continue
        else:
            words[i].sort()

    for i in range(1, 51):
        if not words[i]: continue
        else:
            for j in range(len(words[i])):
                print(words[i][j])