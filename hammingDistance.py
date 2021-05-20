def hammingDistance(x,y):
    x = '{:032b}'.format(x)
    y = '{:032b}'.format(y)
    count = 0
    for i in range(32):
        if x[i] != y[i]:
            count+=1
    return count