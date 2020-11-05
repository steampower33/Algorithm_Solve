
s = input()

def confirm(s):

    i = 0
    a = 0
    while i < len(s):
        if s[i] == 'c':
            if s[i+1] == '-' or '=':
                i += 1
                a += 1
        elif s[i] == 'd':
            if s[i+1] == 'z':
                i += 2
                a += 1
        elif s[i] == 'd':
            if s[i+1] == '-':
                i += 1
                a += 1
        elif s[i] == 'l' and s[i+1] == 'j':
            i += 1
            a += 1
        elif s[i] == 'n' and s[i+1] == 'j':
            i += 1
            a += 1
        elif s[i] == 's' and s[i+1] == '=':
            i += 1
            a += 1
        elif s[i] == 'z' and s[i+1] == '=':
            i += 1
            a += 1
        else:
            a += 1
        i += 1

    return print(a)

confirm(s)