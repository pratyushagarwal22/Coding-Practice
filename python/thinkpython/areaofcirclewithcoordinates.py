'''
Write a function that takes two points, the center of the circle and a
point on the perimeter, and computes the area of the circle.
'''

import math

def circle_radius():
  print('Enter coordinates of the Center: ')
  xc = float(input())
  yc = float(input())
  print('Enter coordinates of the Perimeter: ')
  xp = float(input())
  yp = float(input())

  dx = xc-xp
  dy = yc-yp
  radius = math.sqrt(math.pow(dx,2)+math.pow(dy,2))
  return radius


def circle_area():
  radius = circle_radius()
  area = math.pi * math.pow(radius,2)
  print('Area of Circle is: ', area)

circle_area()