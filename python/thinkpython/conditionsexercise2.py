'''
If any of the three lengths is greater than the sum of the other two, then you cannot
form a triangle. Otherwise, you can. (If the sum of two lengths equals the third, they
form what is called a “degenerate” triangle.)

'''

def is_triangle():
  a = int(input())
  b = int(input())
  c = int(input())
  
  if (a+b)<c or (b+c)<a or (a+c)<b:
    print('Triangle Not Possible')
  else:
    print('Triangle Possible')

is_triangle()