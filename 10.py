## Project Euler
## Problem 10
##
## The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
##
## Find the sum of all the primes below two million.

from math import log as ln

n = 2000000

candidates = list(range(n+1))

for x in xrange(2, int(n**0.5)+1):
  if candidates[x]:
    candidates[(x*2)::x] = [0]*(n//x-1)
    
print "Euler answer is:", sum(i for i in candidates if i >= 2)
