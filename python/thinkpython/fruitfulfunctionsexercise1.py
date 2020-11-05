''' 
Write a function named ack
that evaluates Ackermann’s function. Use your function to evaluate ack(3, 4), which should be
125. What happens for larger values of m and n?
'''

def ack(m,n):
  if m == 0:
    return n+1
  elif m > 0 and n == 0:
    return ack(m-1,1)
  elif m > 0 and n > 0:
    return ack(m-1,ack(m,n-1))
  else:
    pass

ans = ack(3,4)
print(ans)