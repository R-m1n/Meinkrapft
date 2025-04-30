# Return the maximum value over all triplets of indices (i, j, k) such that i < j < k. If all such triplets have a negative value, return 0.
# The value of a triplet of indices (i, j, k) is equal to (nums[i] - nums[j]) * nums[k].

# In score = (x - y) * z the idea is to find y such that it maximizes the score, for each x that is the maximum up until y and z that is the maximum from y to the end of the list.

nums = [16,2,10,20,16,2,13,8,19]

n = len(nums)

left_max = [0] * n
left_max[0] = nums[0]
for i in range(1, n):
    left_max[i] = max(left_max[i - 1], nums[i])

right_max = [0] * n
right_max[-1] = nums[-1]
for i in range(n - 2, -1, -1):
    right_max[i] = max(right_max[i + 1], nums[i])

ans = 0
for i in range(1, n - 1):
    left = left_max[i - 1]
    right = right_max[i + 1]
    ans = max(ans, (left - nums[i]) * right)
