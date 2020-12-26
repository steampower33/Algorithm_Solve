import collections, sys

if __name__ == "__main__":

    t = int(sys.stdin.readline())

    for i in range(t):
        f = list(sys.stdin.readline())
        l = int(sys.stdin.readline())
        nums = collections.deque(sys.stdin.readline().rstrip('\n').strip('[]').split(','))
        result = 0
        ReverseStack = 0

        for j in f:
            if j == 'R':
                ReverseStack += 1
            elif j == 'D':
                if l > 0:
                    if ReverseStack % 2 == 1:
                        nums.pop()
                    elif ReverseStack % 2 == 0:
                        nums.popleft()
                    l -= 1
                else:
                    result = 'error'
                    break

        if ReverseStack % 2 == 1:
            nums.reverse()
        elif ReverseStack % 2 == 0:
            ...

        if result == 'error':
            print(result)
        else:
            print('[',end='')
            for k in range(len(nums)):
                if k == len(nums) - 1:
                    print(nums[k], end='')
                else:
                    print(nums[k], end=',')
            print(']')

