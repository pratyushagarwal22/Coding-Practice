'''
The provided code stub reads and integer, n, from STDIN. For all non-negative integers i<n, print i^2.

'''
import math

val = int(input())
n = abs(val)

for i in range(n):
  print(int(math.pow(i,2)))

