import collections, sys

if __name__ == "__main__":

    nums = collections.deque(sys.stdin.readline().rstrip('\n').strip('[]').split(','))

    print(nums)