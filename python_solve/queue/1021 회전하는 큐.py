
if __name__ == "__main__":
    f = lambda : map(int, input().split())
    n,m = f()
    nums = [*range(1, n+1)]

    idx = 0
    cnt = 0

    for _ in f():
        wantNumIndex = nums.index(_)
        t1 = abs(wantNumIndex - idx)
        t2 = len(nums) - t1
        cnt += min(t1, t2)
        idx = wantNumIndex
        del nums[wantNumIndex]
    print(cnt)

