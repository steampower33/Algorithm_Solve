def rob(nums):
    if not nums: return 0
    def m(nums):
        nums = [0] + nums
        for i in range(3, len(nums)):
            nums[i] += max(nums[i - 3], nums[i - 2])
        return max(nums[-1], nums[-2])
    return max(m(nums[1:]), m(nums[:-1])) if len(nums) > 2 else max(nums)

if __name__ == "__main__":
    print(rob([1,2,3,1,2,5]))
