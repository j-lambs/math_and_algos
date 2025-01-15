# How many possible conbinations of "coins" that add up to 200
def getSmallerCoinsThanN(n, coins):
    return {c for c in coins if c <= n}

def countCoinCombos(n):
    coins = {1, 2, 5, 10, 20, 50, 100, 200}
    coins_used = {}
    count = countCoinCombosHelper(n, 0, getSmallerCoinsThanN(n, coins), coins_used)
    return count

# i can return an array of hashmaps, key = gbp coin, val = num of coins used
#TODO: build a list of coins used in each sequence
def countCoinCombosHelper(n, count, coins, coins_used):

    # Base Case
    if n == 0:
        count += 1
        print(coins_used)
        return count
    if n == 1:
        count += 1
        coins_used[1] = coins_used.get(1) + 1
        print(coins_used)
        return count

    # countCoinCombinationsHelper(n - coin_i)
    for coin in coins:
        if coin in coins_used:
            coins_used[coin] = coins_used.get(coin) + 1
        else:
            coins_used[coin] = 1
        count =+ countCoinCombosHelper(n - coin, count, getSmallerCoinsThanN(n - coin, coins), coins_used)
    return count

print(countCoinCombos(5))

