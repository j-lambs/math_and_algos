# Input: cost = [10,15,20]
# Output: 15
# Explanation: You will start at index 1.
# - Pay 15 and climb two steps to reach the top.
# The total cost is 15.

# Input: cost = [1,100,1,1,1,100,1,1,100,1]
# Output: 6

def minCostClimbingStairs(cost) -> int:
    memo = dict()
    if len(cost) == 2:
        return min(cost[0], cost[1])
    return minCostClimbingStairsHelper(cost=cost, i=0, memo=memo)

def minCostClimbingStairsHelper(cost, i, memo:dict) -> int:
    top_floor = len(cost)
    if memo.get(i) is not None:
        return memo.get(i)
    elif top_floor == i:
        memo.update({i: cost[i]})
        return 0
    elif i >= top_floor - 2:
        memo.update({i: cost[i]})
        return cost[i]
    else:
        cur_step_cost = cost[i] + min(minCostClimbingStairsHelper(cost, i + 1, memo),
                                 minCostClimbingStairsHelper(cost, i + 2, memo))
        memo.update({i: cur_step_cost})
        if i == 0:
            return min(memo.get(0), memo.get(1))
        else:
            return memo.get(i)
    

# at each step, you can go either 1 or 2 steps
# return cost of remaining 'stairs', see whichever has smallest cost
cost = [1,100,1,1,1,100,1,1,100,1]
# cost = [10, 15, 20, 10]
# cost = [4, 2]
print(min(cost))
# print(minCostClimbingStairs(cost))

