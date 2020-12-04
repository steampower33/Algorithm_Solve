import sys

if __name__ == "__main__":
    while True:
        s = list(sys.stdin.readline())
        result = True
        check = list()
        if s[0] == '.':
            break
        for i in s:
            if i == '(':
                check.append('(')
            elif i == '[':
                check.append('[')
            elif i == ')':
                if len(check) == 0:
                    result = False
                    break
                elif check[-1] == '(':
                    check.pop()
                else:
                    result = False
                    break
            elif i == ']':
                if len(check) == 0:
                    result = False
                    break
                elif check[-1] == '[':
                    check.pop()
                else:
                    result = False
                    break

        if len(check) == 0 and result == True:
            print('yes')
        elif result == False:
            print('no')
        elif len(check) > 0 and result == True:
            print('no')


        s.clear()
        check.clear()