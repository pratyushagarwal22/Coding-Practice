'''function program using function objects'''
def do_twice(fobj, val):
  fobj(val)
  fobj(val)

def print_val(s):
  print(s)

do_twice(print_val, 'spam')

def do_four():
  do_twice(print_val, 'four times print')
  do_twice(print_val, 'four times print')

do_four()