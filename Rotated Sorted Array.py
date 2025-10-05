def search_rotated_array(nums, target):
    low, high = 0, len(nums) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if nums[mid] == target:
            return mid
        
        # Left side is sorted
        if nums[low] <= nums[mid]:
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        # Right side is sorted
        else:
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    
    return -1

# Example
nums = [4,5,6,7,0,1,2]
target = 0
print(search_rotated_array(nums, target))  # Output: 4
