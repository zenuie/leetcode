def sortArrayByParity(A):
    even = []
    odd = []
    # for i in A:
    #     if i%2 ==0:
    #         even.append(i)
    #     else:
    #         odd.append(i)
    # return even+odd
    even = [even for even in A if even%2 == 0]
    odd = [odd for  odd in A if odd%2 !=0]
    return even+odd
sortArrayByParity([3,1,2,4])