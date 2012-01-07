#!/usr/bin/python
# -*- coding: UTF-8 -*-
## Project Euler
## Problem 341
##
## The Golomb's self-describing sequence {G(n)} is the only
## nondecreasing sequence of natural numbers such that n
## appears exactly G(n) times in the sequence. The values of
## G(n) for the first few n are:
##
## n	  1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	…
## G(n)	1	2	2	3	3	4	4	4	5	5	5	6	6	6	6	…
##
## You are given that G(10^3) = 86, G(10^6) = 6137.
## You are also given that ΣG(n^3) = 153506976 for 1 ≤ n < 10^3.
##
## Find ΣG(n^3) for 1 ≤ n < 10^6.

# integral(e^(ln(x^3/0.7601940604611106)/1.6139299999999999) from 1 to 10^3)
# 1.5633x10^8 which is close to 153506976

# integral(e^(ln(x^3/0.7601940604611106)/1.6139299999999999) from 1 to 10^6)

import math

a = 1.2051490956493400684373472380642007495518983216555320189017
#b = 0.6178192240134547099980032659628268267776204291239465464529
b = (1 + (5 ** 0.5))/2
f = lambda x: a*(x ** (3*b))
f2 = lambda x: b**(2-b)*x**((b-1))

class queue(object):

  class node:
    def __init__(self, value, count):
      self.value = value
      self.count = count
      self.next = None
    
  def __init__(self):
    self.head = None
    self.tail = None
    
  def add(self, value, count):
    new = self.node(value, count)
    if self.tail is not None:
      self.tail.next = new
    if self.head is None:
      self.head = new
    self.tail = new
    
  def remove(self):
    if self.head.count == 0:
      self.head = self.head.next
    self.head.count -= 1
    return self.head.value
    
  def __str__(self):
    s = []
    n = self.head
    while n is not None:
      s.append("({},{})".format(n.value, n.count))
      n = n.next
    return ", ".join(s)

def myxrange(start, end, step):
  n = start
  while n < end:
    yield n
    n += step

def golomb():
  yield 1
  yield 2
  # [value, count] pair
  # value is the value of G(n)
  # count is how many more occurrances of value are left in the sequence
  g = queue()
  g.add(2, 1)
  ix = 3
  while True:
    try:
      next = g.remove()
    except IndexError:
      return
    g.add(ix, next)
    ix += 1
    yield next

def golomb_sum(n):    
  g = golomb()
  total = 0
  prev_cube = 0
  for x in xrange(1, n+1):
    for y in xrange(x**3 - prev_cube):
      n = g.next()
    total += n
    prev_cube = x **3
  return total
  
# golomb_sum(10**6)

"""g = golomb()
for x in myxrange(0, 10**18, 1):
  if x % 1000 == 0:
    print x
  g.next()
"""

def growth(mx):
  # Grows at an exponential rate
  from collections import defaultdict
  
  g = golomb()
  d1 = defaultdict(int)
  
  for x in xrange(1, mx):
    n = g.next()
    d1[n] += 1
    
  d2 = defaultdict(int)
  
  for x in d1:
    d2[d1[x]] += 1
    
  d3 = defaultdict(int)
  for x in d2:
    d3[d2[x]] += 1
    
  
  for x in d3:
    print x, d1[x], d2[x], d3[x]
    
  f = open("a.csv", 'w')
  for x in d1:
    f.write("{},{},{},{}\n".format(x, d1[x],d2[x],d3[x]))
  f.close()

#growth(10 **6)


def integration():
  import scipy.integrate

  def percent_error(actual, expected):
    return (actual - expected)/expected

  def pprint(bound, sample_sum, sample_max):
    sm = scipy.integrate.quad(f2, 1, bound)[0]
    print("For 1<=n<={}:\n"
          "  Real:\t    {}\n"
          "  Expected: {}\n"
          "  Percent Error: {}".format(
            bound,
            sm,
            sample_sum,
            percent_error(sm-sample_max, sample_sum)))

  pprint(10**3, 153506976, 86)

#integration()
g = golomb()
mod = 0
for x in xrange(1,10**3):
  n = g.next()
  t = f2(x)
  if round(t)-mod != n:
    print t, mod, n, x
  elif t - round(t) > 0.4:
    print t

#print f2(10**18)
print "NOT COMPLETE."
