''' Write a program to find the nth term of fibonacci series'''

def print_fibonacci(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return print_fibonacci(n-1) + print_fibonacci(n-2)

val = print_fibonacci(6)
print(val)