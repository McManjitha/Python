def insertion_sort(nums):
    # making a copy
    nums = list(nums)

    for i in range(len(nums)):

        j = i - 1 
        curl = nums.pop(i)

        while(j >= 0 and nums[j] > curl):
            j -= 1
        
        nums.insert(j+1, curl)
    
    return nums

list1 = [4, 2, 6, 3, 4, 6, 2, 1]
print(insertion_sort(list1))
