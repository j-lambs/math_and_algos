
def countCoinCombinations(n):
    count = countCoinCombinationsHelper(n, 0)
    return count - (int)((count - 2) / 2)

def countCoinCombinationsHelper(n, count):
    vals = []
    for i in range(1, n + 1):
        vals.append(i)

    # Base Case
    if n < 0:
        return 0
    if n == 0 or n == 1:
        count += 1
        return count

    # countCoinCombinationsHelper(n - coin_i)
    for val in vals:
        count =+ countCoinCombinationsHelper(n - val, count)
    return count


n = 4

print(countCoinCombinations(n))
