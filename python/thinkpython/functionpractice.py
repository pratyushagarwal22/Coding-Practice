'''Basic function definition and call'''

def print_lyrics():
  print('this is statement 1')
  print('this is statement 2')

def repeat_lyrics():
  print_lyrics()
  print_lyrics()

repeat_lyrics()

'''Accepting arguments and parameters'''

var1 = "this is the first variable"
def accept_argument(value):
  print(value)
  print(value)

accept_argument(var1)

'''local variables'''
val1 = 'hello world'
val2 = 'world hello'
def localvariable(val1, val2):
  sentence = val1 + val2
  print(sentence)

localvariable(val1, val2)