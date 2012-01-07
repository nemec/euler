## Project Euler
## Problem 3
##
## The prime factors of 13195 are 5, 7, 13 and 29.
##
## What is the largest prime factor of the number 600851475143 ?

import sys
from random import random

def gcd(a, b):
  if a % b == 0:
    return b
  return gcd(b, a%b)

# http://en.wikipedia.org/wiki/Pollard%27s_rho_algorithm
def f(x, n):
  """ Psuedorandom transformation function """
  return (pow(x, 2) + 1) % n

n = 600851475143

while True:
  factors = set()

  while True:
    x = 2
    y = 2
    d = 1

    while d == 1:
      x = f(x, n)
      y = f(f(y, n), n)
      d = gcd(abs(x-y), n)

    if d == n or d in factors:
      break
    else:
      factors.add(d)

  if len(factors) == 0:
    break

  c = max(factors)
  n = max(n/c, c)

print "Euler answer is:", n
