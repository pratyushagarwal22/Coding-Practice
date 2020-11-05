
def b(z): # 9
  prod = a(z, z) # 90
  print(z, prod)
  return prod

def a(x, y):
  x = x + 1
  return x * y

def c(x, y, z): # 1, 5, 3
  total = x + y + z # 9
  square = b(total)**2
  return square

x = 1
y = x + 1
print(c(x, y+3, x+y)) # 1, 5, 3