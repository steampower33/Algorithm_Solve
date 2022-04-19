def deleteAndEarn(nums):
    ans = 0

    sums = [0] * 10001

    for num in nums:
        sums[num] += num

    val = sums[0]
    val_1 = 0

    print(sums)
    for _ in range(1, len(sums)):
        val_1, val_2 = val, val_1
        val = max(sums[_] + val_2, val_1)

    return val

print(deleteAndEarn([2,2,3,3,3,4]))