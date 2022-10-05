def merge_sort(nums):
    nums = list(nums)

    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2

    left = nums[:mid]
    right = nums[mid:]

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return merge(left_sorted, right_sorted)


def merge(left_nums, right_nums):
    new_list = []
    i = 0
    j = 0
    
    while i < len(left_nums) and j < len(right_nums):

        if left_nums[i] >= right_nums[j]:
            new_list.append(right_nums[j])
            j += 1

        elif left_nums[i] <= right_nums[j]:
            new_list.append(left_nums[i])
            i += 1

    return new_list + right_nums[j:] + left_nums[i:]


list_1 = [5, -12, 2, 6, 1, 23, 7, 7, -12, 6, 12, 1, -243, 1, 0]
print(merge_sort(list_1))
        

