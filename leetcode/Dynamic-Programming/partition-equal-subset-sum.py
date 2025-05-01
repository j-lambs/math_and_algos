
def can_partition(nums: list) -> bool:
    target = sum(nums) / 2
    myset = set()
    myset.add(0)
    
    for i in nums:
        # myset.add(i)
        temp = []
        for elt in myset:
            if elt + i == target:
                return True
            temp.append(elt + i)
        for elt in temp:
            myset.add(elt)
    
    if target in myset:
        return True
    else:
        return False

# nums = [1,5,11,5]
nums = [1,2,5]
print(can_partition(nums))
