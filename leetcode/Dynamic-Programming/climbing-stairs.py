
def climb_stairs(n: int) -> int:
    memo = dict()
    return climb_stairs_helper(n, memo)

def climb_stairs_helper(n: int, memo: dict) -> int:
    if (n == 2):
        return 2
    elif (n <= 1):
        return n
    elif (memo.get(n)) is not None:
        return memo.get(n)
    else:
        current_stair_permutations = climb_stairs_helper(n - 1, memo) + climb_stairs_helper(n - 2, memo)
        memo.update({n: current_stair_permutations})
        return current_stair_permutations

print(climb_stairs(3))
