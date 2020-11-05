def selectionSort(nums):
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] < nums[j]: continue
            else:
                nums[i], nums[j] = nums[j], nums[i]

    return nums

if __name__ == "__main__":

    while True:
        x, y, z = map(int, input().split())
        if x == 0 and y == 0 and z == 0: break

        value = selectionSort([x,y,z])

        if (value[0]**2 + value[1]**2) == value[2]**2: print("right")
        else: print("wrong")

