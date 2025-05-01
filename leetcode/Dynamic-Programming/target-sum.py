
def find_target_num_ways(nums: list, target: int) -> int:
    num_paths = 0
    sums = [0]

    for elt in nums:
        temp_sums = []
        for i in range(len(sums)):
            temp_sums.append(elt + sums[i])
            temp_sums.append(-1 * elt + sums[i])
        sums = temp_sums
    
    for s in sums:
        if s == target:
            num_paths += 1
    
    return num_paths


nums = [1,1,1,1,1]
target = 3

print(f'Number of ways to add up to {target}: {find_target_num_ways(nums, target)}')