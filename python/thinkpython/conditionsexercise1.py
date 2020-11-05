'''
Write a function named check_fermat that takes four parameters—a, b, c and n—and that checks to see if Fermat’s theorem holds.

Fermats Theorem: a^n + b^n = c^n
'''
import math

def check_fermat():
  a = int(input())
  b = int(input())
  c = int(input())
  n = int(input())

  finval = math.pow(a,2) + math.pow(b,2)
  if finval == math.pow(c,2) and n>2:
    print('Holy Smokes, Fermat was Wrong!')
  else:
    print('No, that doesn\'t work')
  
check_fermat()
