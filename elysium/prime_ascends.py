
import math
import bisect

nums = [998,2]

primes = []

def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
        
    return True

for i in range(2, 1001):
    if is_prime(i):
        primes.append(i)
        
def is_increasing(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        if not (arr[left] < arr[left + 1] and arr[right - 1] < arr[right]):
            return False
        
        left += 1
        right -= 1

    return True

def primeSubOperation(nums, primes):
    for i in range(len(nums)):
        terminators = [
            nums[i] == 1 and i != 0,
            nums[i] == 2 and i != 0 and i != 1,
            i != 0 and nums[i] <= nums[i - 1],
        ]

        if any(terminators):
            return False

        left_idx = bisect.bisect_left(primes, nums[i])

        for j in range(left_idx, -1, -1):
            update = nums[i] - primes[j]

            if i == 0:
                nums[i] = update

                break

            if nums[i-1] < update:
                nums[i] = update

                break

    return True

print(len(primes))
primeSubOperation(nums, primes)
print(nums)