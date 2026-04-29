def list_of_largest(nums, nums2):
    result = []
    for i in range(len(nums)):
        result.append(max(nums[i], nums2[i]))
    return result
