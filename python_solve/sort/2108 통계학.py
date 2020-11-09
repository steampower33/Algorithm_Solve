import sys

def quickSort(nums):
    if len(nums) <= 1: return nums
    pivot = nums[len(nums) // 2]
    lesser, equal, greater = [], [], []
    for num in nums:
        if num < pivot:
            lesser.append(num)
        elif num > pivot:
            greater.append(num)
        else:
            equal.append(num)
    return quickSort(lesser) + equal + quickSort(greater)

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    nums = list()
    numsCount = [0 for i in range(8001)]
    mode = 0
    count = 0

    for i in range(N):
        num = int(sys.stdin.readline())
        nums.append(num)
        numsCount[4000 + num] += 1

    nums = quickSort(nums)
    maxCount = max(numsCount)

    for i in range(len(numsCount)):
        if numsCount[i] == maxCount:
            mode = i-4000
            count += 1
            if count == 2: break

    print(round(sum(nums) / N))
    print(nums[len(nums)//2])
    print(mode)
    print(abs(nums[0]-nums[len(nums)-1]))