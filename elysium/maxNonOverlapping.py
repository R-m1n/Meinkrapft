
# nums = [1,1,1,1,1]
# target = 2

# nums = [-1,3,5,1,4,2,-9]
# target = 6

nums = [-2,6,6,3,5,4,1,2,8]
target = 10

def divide(array, target):
    count = 0

    if len(array) == 1:
        return 1 if array[0] == target else 0

    mid_index = len(array) // 2

    if sum(array) == target:
        count += 1

    print(array)

    left = divide(array[:mid_index], target)
    right = divide(array[mid_index:], target)

    return count + left + right

def maxNonOverlapping(nums, target):
    prefix_map = {0: -1}
    current_sum = 0
    count = 0
    last_end = -1

    for i, num in enumerate(nums):
        current_sum += num
        required = current_sum - target
        
        if required in prefix_map:
            start = prefix_map[required] + 1
            if start > last_end:
                count += 1
                last_end = i
                # Reset the prefix map to avoid overlaps
                prefix_map = {current_sum: i}
                continue

        # Only add to prefix_map if not updated in this iteration
        if current_sum not in prefix_map:
            prefix_map[current_sum] = i

    return count

# if not (len(nums) % 2 == 0):
#     nums.append(0)

print(maxNonOverlapping(nums, target))