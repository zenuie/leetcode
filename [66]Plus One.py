def plusOne(digits):
    for i in range(len(digits) - 1, -1, -1):
        if sum(digits) == 9 * len(digits): return [1]+[0 for i in range(len(digits))]
        if digits[i] == 9 and len(digits) != 1:
            digits[i] = 0
        else:
            digits[i] += 1
        print(digits)


plusOne([9])
