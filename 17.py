## Project Euler
## Problem 17
##
## If the numbers 1 to 5 are written out in words: one, two, three, four, five,
## then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
##
## If all the numbers from 1 to 1000 (one thousand) inclusive were written
## out in words, how many letters would be used?
##
## NOTE: Do not count spaces or hyphens. For example, 342 (three hundred
## and forty-two) contains 23 letters and 115 (one hundred and fifteen)
## contains 20 letters. The use of "and" when writing out numbers is in
## compliance with British usage.


digits = ("one", "two", "three", "four", "five", "six", "seven", "eight",
          "nine")
          
teens = ("ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
        "seventeen", "eighteen", "nineteen")
        
tens = ("twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty",
        "ninety")

# Hardcoded
"""
def add(it):
  return sum(map(len, it))

total = 0

digit_sum = add(digits) # 1-9
total += digit_sum

teen_sum = add(teens) # 10-19
total += teen_sum

ten_sum = add(tens)

hun_sum = len(tens) * digit_sum + (len(digits)+1) * ten_sum # 1-99
total += hun_sum

total *= len(digits) + 1

total += digit_sum * 100

total += len("hundred") * 100 * len(digits)
total += len("and") * 99 * len(digits)

total += len("one") + len("thousand")
print total
"""

def brute(i):
  if i == 0:
    return ""
  elif i == 1000:
    return "onethousand"
  elif i >= 100:
    s = ""
    hun = i // 100
    s += digits[hun-1] + "hundred"
    i -= 100 * hun
    if i > 0:
      s += "and"
      s += brute(i)
    return s
  elif i >= 20:
    ten = i // 10
    return tens[ten-2] + brute(i - ten * 10)
  elif i >= 10:
    return teens[i-10]
  else:
    return digits[i-1]

print "Euler answer is:", sum(len(brute(x)) for x in xrange(1, 1001))
