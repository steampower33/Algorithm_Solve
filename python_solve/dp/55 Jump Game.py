
def canJump(nums):
    max_acc_num = 0
    for _ in range(len(nums)):
        if max_acc_num < _: return False
        acc_num = _ + nums[_]
        if max_acc_num < acc_num: max_acc_num = acc_num

        if len(nums)-1 <= max_acc_num: return True

    return False

print(canJump([0]))