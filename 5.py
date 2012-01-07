## Project Euler
## Problem 5
##
## 2520 is the smallest number that can be divided by
## each of the numbers from 1 to 10 without any remainder.
##
## What is the smallest positive number that is evenly
## divisible by all of the numbers from 1 to 20?

# always divisible by 1
mx = 20
nums = range(2, mx+1)

def gcd(a, b):
  if a % b == 0:
    return b
  return gcd(b, a%b)

finished = False
while not finished:
  finished = True
  for x in nums:
    for y in nums:
      if x > y:
        if x % y == 0:
          nums.remove(y)
          finished = False
          continue
        d = gcd(x, y)
        if d > 1:
          nums.append(x*y/d)
          nums.remove(x)
          nums.remove(y)
          finished = False
          break
  
try:
  from functools import reduce
except:
  pass  # Just use the built-in reduce instead
from operator import mul

print "Euler solution is:", reduce(mul, nums)
