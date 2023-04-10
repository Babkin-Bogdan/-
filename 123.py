nums = [0, 1, 0, 3, 12]

zeros = 0
for num in nums:
    if num == 0:
        zeros += 1

i = 0
for num in nums:
    if num != 0:
        nums[i] = num
        i += 1

for j in range(zeros):
    nums[i + j] = 0

print(nums) # [1, 3, 12, 0, 0]
