def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    random = nums.pop()
    left = []
    right = []

    for i in nums:
        if i <= random:
            left.append(i)
        else:
            right.append(i)

    return merge_sort(left) + [random] + merge_sort(right)
    


list_1 = [5, -12, 2, 6, 1, 23, 7, 7, -12, 6, 12, 1, -243, 1, 0]
print(merge_sort(list_1))


    