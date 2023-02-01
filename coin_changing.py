import sys
sys.setrecursionlimit(10000)

# Some coin systems:

arbitrary_coins = [1,2,5,7]
sterling_coins = [1,2,5,10,20,50,100,200]

c_list = arbitrary_coins

# Plain recursive implementation

def fewest_coins(v):
    if (v == 0):
        return 0
    res = sys.maxsize

    for i in range(0, len(c_list)):
        if (c_list[i] <= v):
            sub_res = fewest_coins(v-c_list[i])
            print(sub_res)

            if (sub_res != sys.maxsize and sub_res + 1 < res):
                res = sub_res + 1
    return res

print(fewest_coins(22))

# Memoization operation

def memoize(f):
    memo = {}
    def check(v):
        if v not in memo:
            memo[v] = f(v)
        return memo[v]
    return check

# To get the optimization of the recursion:

fewest_coins = memoize(fewest_coins)
print(fewest_coins(100))

# Note: If c_list is changed, the "cache" used by the memoized function will no longer be valid.
#   --> Would need to reload the file within the Python interpreter to use with new c_list.

# From-scratch memoization implementation (without using higher-order function "memoize")

def fewest_coins_dp(v):
    C = [sys.maxsize] * (v + 1)
    P = [sys.maxsize] * (v + 1)
    C[0] = 0
    C[1] = 1
    P[1] = 0

    for p in range(2, v+1):
        for i in range(0,len(c_list)):
            if(c_list[i] <= p and (C[p - c_list[i]] + 1) < C[p]):
                C[p] = C[p - c_list[i]] + 1
                P[p] = i
    return C[len(C)-1]

# This implementation returns the specific coins that make up the most effective change combination.

def fewest_coins_list_dp(v):
    C = [sys.maxsize] * (v + 1)
    P = [sys.maxsize] * (v + 1)
    C[0] = 0
    C[1] = 1
    P[1] = 0
    result = [0] * len(c_list)

    for p in range(2, v+1):
        for i in range(0,len(c_list)):
            if(c_list[i] <= p and (C[p - c_list[i]] + 1) < C[p]):
                C[p] = C[p - c_list[i]] + 1
                P[p] = i
    
    while v > 0:
        i = P[v]
        result[i] += 1
        v -= c_list[i]

    return result

print(fewest_coins_list_dp(13))
