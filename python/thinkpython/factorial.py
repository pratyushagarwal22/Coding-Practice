''' 
Write a program to evaluate the factorial of a number n 
This program demonstrates a pattern called as 'guardian'
'''

def calc_factorial(n):
  if not isinstance(n, int):
    print('Factorial is only defined for Integers')
  elif n < 0:
    print('Factorial is not defined for negative Integers')
  elif n == 0:
    return 1
  else:
    recurse = calc_factorial(n-1)
    result = n*recurse
    return result

ans = calc_factorial(10)
print(ans)