__author__ = 'nsrivas3'


def isPowerOfTwo(n):
    if n == 0: return(False)
    if n == 1: return(True)
    counter = 0
    while(counter==0 and n!=1):
        counter = n%2
        n = int(n/2)
    if n==1 and counter==0: return(True)
    else: return(False)

print(isPowerOfTwo(32))
