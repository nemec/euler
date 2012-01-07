## Project Euler
## Problem 7
##
## By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
## we can see that the 6th prime is 13.
##
## What is the 10001st prime number?

import random
from math import log as ln
import math

n = 10001

def mine(n):
  # Upper bound on the nth prime value
  # http://en.wikipedia.org/wiki/Prime_number_theorem#Approximations_for_the_nth_prime_number
  n = int(n * ln(n) + n * (ln(ln(n))))
  primes = [2]
  
  def is_prime(primes, x):
    for y in primes:
      if x % y == 0:
        return False
    return True
  
  for x in xrange(3, n, 2):
    if is_prime(primes, x):
      primes.append(x)
  return primes

def ext(n):
  n = int(n * ln(n) + n * (ln(ln(n))))

  candidates = list(range(n+1))
  fin = int(n**0.5)

  # Loop over the candidates, marking out each multiple.
  for i in xrange(2, fin+1):
      if candidates[i]:
          candidates[2*i::i] = [None] * (n//i - 1)

  # Filter out non-primes and return the list.
  return [i for i in candidates[2:] if i]
  
primes = mine(n)
if len(primes) >= 10000:
  print "Euler solution is:", primes[10000]
else:
  print "Not enough primes: {}.".format(len(primes))
