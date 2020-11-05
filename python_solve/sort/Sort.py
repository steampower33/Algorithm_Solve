# 선택 정렬 시간 : O(n^2), 공간 : O(n)
def selectionSort(nums):
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] < nums[j]:
                continue
            else:
                nums[i], nums[j] = nums[j], nums[i]

    print(nums[0], nums[len(nums)-1])

# 삽입 정렬 시간 : O(n^2), 공간 : O(n)
def insertionSort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        for j in reversed(range(i)):
            if nums[j] > key: nums[j], nums[j+1] = nums[j+1], nums[j]

    print(nums[0], nums[len(nums)-1])

# 버블 정렬 시간 : O(n^2), 공간 : O(n)
def bubbleSort(nums):
    for i in range(len(nums)):
        for j in range(len(nums)-1):
            if nums[j] > nums[j+1]: nums[j], nums[j+1] = nums[j+1], nums[j]

    print(nums[0], nums[len(nums)-1])

# 합병 정렬 시간 : 합병과정 - O(n1 + n2) = O(n) 분할 과정 O(lgN) -> O(NlgN) 공간 : O(2n)
def mergeSort(nums):
    def merge(left, right):
        result = []
        while len(left) > 0 or len(right) > 0:
            if len(left) > 0 and len(right) > 0:
                if left[0] > right[0]:
                    result.append(right[0])
                    right = right[1:]
                else:
                    result.append(left[0])
                    left = left[1:]
            elif len(left) > 0:
                result.append(left[0])
                left = left[1:]
            elif len(right) > 0:
                result.append(right[0])
                right = right[1:]

        return result

    def merge_divide(nums):
        if len(nums) <= 1: return nums

        m = len(nums) // 2
        left = nums[:m]
        right = nums[m:]

        left = merge_divide(left)
        right = merge_divide(right)

        return merge(left, right)

    result = merge_divide(nums)
    print(result[0], result[len(result) - 1])

# 퀵 정렬 시간 : O(NlgN) ~ O(N^2) 공간 : O(n)
def quickSort(nums):
    def quick(nums):
        if len(nums) <= 1:
            return nums
        pivot = nums[len(nums) // 2]
        lesser, equal, greater = [], [], []
        for num in nums:
            if num < pivot:
                lesser.append(num)
            elif num > pivot:
                greater.append(num)
            else:
                equal.append(num)
        return quick(lesser) + equal + quick(greater)

    result = quick(nums)
    print(result[0], result[len(result)-1])

if __name__ == "__main__":
    nums = list(map(int, input().split()))

    # 선택 정렬
    #selectionSort(nums)

    # 삽입 정렬
    #insertionSort(nums)

    # 버블 정렬
    # bubbleSort(nums)

    # 합병 정렬
    # mergeSort(nums)

    # 퀵 정렬
    quickSort(nums)
