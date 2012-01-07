## Project Euler
## Problem 9
##
## A Pythagorean triplet is a set of three natural numbers, a < b < c,
## for which, a^2 + b^2 = c^2
## 
## For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
## 
## There exists exactly one Pythagorean triplet for which a + b + c = 1000.
## Find the product abc.

## b = (-per^2+2*a*per)/(2*(a-per))

per = 1000

for a in xrange(1, per // 3 + 2):
  b = (-per**2+2*a*per)//(2*(a-per))
  c = int(((a**2)+(b**2))**0.5)
  if sum((a, b, c)) == 1000:
    print "Triplet:", a, b, c
    print "Euler answer is:", a*b*c
    break
