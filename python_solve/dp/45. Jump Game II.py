def jump(nums):
    end, cnt, max_num = 0, 0, 0;
    for _ in range(len(nums)):
        max_num = max(max_num, _+nums[_])

        if len(nums) == 1: return 0

        if _ == end:
            end = max_num
            cnt += 1

        if len(nums)-1 <= end:
            return cnt

print(jump([0]))