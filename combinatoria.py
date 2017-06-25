def C(n,k):
    
    if n==k or k==0:
        return 1
    if k>n:
        return 0
    if k > n/2:
        return C(n,n-k)
    return C(n-1,k-1) + C(n-1,k)