## Project Euler
## Problem 4
##
## A palindromic number reads the same both ways.
## The largest palindrome made from the product of
## two 2-digit numbers is 9009 = 91 x 99.
##
## Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(n):
  s = str(n)
  for x in xrange(len(s)//2):
    if s[x] != s[-(x+1)]:
      return False
  return True

def find_palindrome(a, b):
  max_palindrome = 0
  mx = pow(10,len(str(a))-1)
  while a >= mx:
    while b >= mx:
      if is_palindrome(a*b):
        if max_palindrome < a*b:
          max_palindrome = a*b
      if b == 91:
        print a, b, "***"
      b -= 1
    a -=1
    b = a
  return max_palindrome

#print "Euler answer is:", find_palindrome(999, 999)

# Brilliant solution from forums:
# 11(9091a + 910b + 100c) = mn
# 0 <= a, b, c < 10 and 100 <= m, n <= 999

# Max m,n = 999/11
# Min m,n = 111/11

def soln():
  mx = 999/11
  mn = 111/11
  for a in xrange(9, 0, -1):
    for b in xrange(9, -1, -1):
      for c in xrange(9, -1, -1):
        num = 9091*a + 910*b + 100*c
        for div in xrange(mx, mn-1, -1):
          if (num % div) == 0:
            if (1.0 * num / div) > 999:
              break
            else:
              return num * 11
  return None
print "Brilliant solution from forums:", soln()
