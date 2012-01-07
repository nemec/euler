## Project Euler
## Problem 1
##
## If we list all the natural numbers below 10
## that are multiples of 3 or 5, we get 3, 5, 6 and 9.
## The sum of these multiples is 23.
##
## Find the sum of all the multiples of 3 or 5 below 1000.

mx = 1000-1

# Based on fact that:
# 1*3 + 2*3 + 3*3 = 3 * (1+2+3)

tot = 0
for x in (3, 5, -15):# Add multiples of 3,5; subtract one set of multiples of 15
  div = mx/x
  sm = 1.0 * (div*(div+1))/2
  tot += sm * x

print "Euler answer is:", tot


