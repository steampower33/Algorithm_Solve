if __name__ == "__main__":
    words = list(map(str, input())) + [None]
    cnt = 0

    for i in range(len(words)):
        if words[i] == None: break
        if words[i] == "l" or words[i] == "n":
            if words[i + 1] == "j": continue
        elif words[i] == "c":
            if words[i + 1] == "=" or words[i + 1] == "-": continue
        elif words[i] == "s" or words[i] == "z":
            if words[i + 1] == "=": continue
        elif words[i] == "d":
            if words[i + 1] == "-": continue
            if words[i + 1] == "z" and words[i + 2] == "=": continue

        cnt += 1

    print(cnt)
