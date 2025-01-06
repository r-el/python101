def find_closest_value(arr, target):
    if not arr:
        return None
    
    left = 0
    right = len(arr) - 1
    
    # If target is less than the smallest element
    if target <= arr[0]:
        return arr[0]
    # If target is greater than the largest element
    if target >= arr[-1]:
        return arr[-1]
        
    while left <= right:
        mid = (left + right) // 2
        
        # If we found the exact value
        if arr[mid] == target:
            return arr[mid]
            
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    # At this point, right points to the largest element smaller than target
    # and left points to the smallest element larger than target
    
    # Compare the differences to find the closest value
    if abs(arr[right] - target) <= abs(arr[left] - target):
        return arr[right]
    else:
        return arr[left]

# Test examples
sorted_array = [1, 2, 4, 5, 7, 8, 9]
print(find_closest_value(sorted_array, 6))  # Should print 5
print(find_closest_value(sorted_array, 3))  # Should print 2
print(find_closest_value(sorted_array, 0))  # Should print 1
print(find_closest_value(sorted_array, 10)) # Should print 9