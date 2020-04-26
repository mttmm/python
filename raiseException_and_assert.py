#raise Exception ('

"""
*************************
*                       *
*                       *
*                       *
*                       *
*************************

"""
# raise exceptions
def boxprint(symbol, width, height):
  if len(symbol) != 1:
    raise Exception('symbol needs to be a string length of 1.')
  if (width < 2) or (height <2):
    raise Exception('width and height must be greater than or equal to 2.')
  print (symbol * width)

  for i in range(height - 2):
    print (symbol + (' ' * (width - 2)) + symbol)
  
  print (symbol * width)

boxprint('$', 1, 1)


# Traceback module will print error messages to file
import traceback
try:
  raise Exception('This is an error message example')
except:
  errorfile = open('c:\\users\\Matt\\Desktop\\errors\\error_log.txt', 'a')
  errorfile.write(traceback.format_exc())
  errorfile.close()
  print('The traceback info was writting to desktop\\errorlog.txt')


  # assertions allow the programmer to test code and raise exceptions
  #assert false, 'This is the error message.'
market_2nd = {'northsouth': 'green', 'eastwest': 'red'}

def switchlights (intersection):
  for key in intersection.keys():
    if intersection[key] == 'green':
      intersection[key] = 'yellow'
    elif intersection[key] == 'yellow':
      intersection[key] = 'red'
    elif intersection[key] == 'red':
      intersection[key] = 'green'
  assert 'red' in intersection.values(), 'Neither light is red!' + str(intersection)

switchlights(market_2nd)
