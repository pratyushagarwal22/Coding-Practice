'''Python If-Else from Hackerrank.
Given an integer, n, perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird
'''

val = input()
intval =  int(val)
def prime_weird(intval):
  if (intval%2==1.0):
    print('Weird')
  elif (intval>=2 and intval<=5):
    print('Not Weird')
  elif (intval>=6 and intval<=20):
    print('Weird')
  elif intval>20:
    print('Not Weird')
  else:
    pass

prime_weird(intval)