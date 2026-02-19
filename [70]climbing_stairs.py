def climbStairs(n):
    base = 0
    next = 1
    result = 0
    while n != 0:
        result = base + next
        base = next
        next = result
        n -= 1
    return result


climbStairs(45)
