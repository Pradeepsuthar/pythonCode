import operator as op

from functools import reduce


n = int(input("Enter N : "))

r = int(input("Enter X : "))



def ncr(n, r):
    
	r = min(r, n-r)
    
	numer = reduce(op.mul, range(n, n-r, -1), 1)
    
	denom = reduce(op.mul, range(1, r+1), 1)
    
	out = numer / denom
    
	ans = int(out)
    
	print (ans)
    


ncr(n,r)